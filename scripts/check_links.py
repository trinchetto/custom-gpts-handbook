#!/usr/bin/env python3
"""Simple link checker for Markdown documentation.

This script walks the repository looking for Markdown files and verifies
that their links remain valid. Internal links are checked for the
existence of the referenced file while external links are requested over
HTTP. The checker is intentionally lightweight and avoids third‑party
packages so it can run in minimal environments.
"""

from __future__ import annotations

import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Iterable, List, Dict

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

@dataclass
class LinkResult:
    url: str
    source: str
    status: str


def _iter_markdown_files(base_dir: str) -> Iterable[str]:
    for root, dirs, files in os.walk(base_dir):
        # Skip hidden directories such as .git or .pytest_cache
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for name in files:
            if name.endswith(".md"):
                yield os.path.join(root, name)


def _extract_links(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    return LINK_RE.findall(text)


def _check_internal(link: str, cwd: str) -> LinkResult | None:
    # Skip pure anchor links such as "#section"
    if link.startswith("#"):
        return None
    target = link.split("#", 1)[0]
    full = os.path.join(cwd, target)
    if os.path.exists(full):
        return LinkResult(link, cwd, "ok")
    return LinkResult(link, cwd, "missing")


def _check_external(link: str, cwd: str) -> LinkResult:
    request = urllib.request.Request(link, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(request, timeout=10) as resp:
            code = resp.getcode()
        if 200 <= code < 400:
            return LinkResult(link, cwd, "ok")
        return LinkResult(link, cwd, f"http {code}")
    except urllib.error.HTTPError as e:
        # Treat 403 (often due to network policy) as a warning rather than failure
        if e.code == 403:
            return LinkResult(link, cwd, "warning 403")
        return LinkResult(link, cwd, f"http {e.code}")
    except Exception:
        # Any other error is treated as a warning
        return LinkResult(link, cwd, "warning")


def check_links(base_dir: str = ".") -> Dict[str, List[LinkResult]]:
    results: Dict[str, List[LinkResult]] = {"failed": [], "warnings": []}
    for md in _iter_markdown_files(base_dir):
        cwd = os.path.dirname(md)
        for link in _extract_links(md):
            if link.startswith("http://") or link.startswith("https://"):
                res = _check_external(link, md)
                if res.status.startswith("http"):
                    results["failed"].append(res)
                elif res.status.startswith("warning"):
                    results["warnings"].append(res)
            else:
                res = _check_internal(link, cwd)
                if res and res.status != "ok":
                    results["failed"].append(res)
    return results


def main() -> int:
    results = check_links()
    for res in results["warnings"]:
        print(f"WARNING: {res.source}: {res.url} -> {res.status}")
    if results["failed"]:
        for res in results["failed"]:
            print(f"BROKEN: {res.source}: {res.url} -> {res.status}")
        return 1
    print("All links look good")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
