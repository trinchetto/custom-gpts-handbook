#!/usr/bin/env python3
"""Check markdown files for broken links."""
import re
import sys
import os
from typing import List, Tuple

import requests

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; LinkChecker/1.0)"}


def find_links(root: str) -> List[Tuple[str, str]]:
    """Return list of tuples (file, url) for all http/https links in markdown files."""
    link_re = re.compile(r"https?://[^\s)]+")
    results: List[Tuple[str, str]] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for filename in filenames:
            if filename.lower().endswith(".md"):
                path = os.path.join(dirpath, filename)
                with open(path, "r", encoding="utf-8") as fh:
                    text = fh.read()
                for url in link_re.findall(text):
                    results.append((path, url))
    return results


def check_link(url: str) -> bool:
    """Return True if URL returns status < 400."""
    try:
        response = requests.head(url, allow_redirects=True, timeout=10, headers=HEADERS)
        if response.status_code >= 400 or response.status_code == 405:
            response = requests.get(url, allow_redirects=True, timeout=10, headers=HEADERS)
        return response.status_code < 400
    except requests.RequestException:
        return False


def get_broken_links(root: str = ".") -> List[Tuple[str, str]]:
    """Return list of (file, url) pairs that could not be reached."""
    broken: List[Tuple[str, str]] = []
    for file, url in find_links(root):
        if not check_link(url):
            broken.append((file, url))
    return broken


def main() -> int:
    broken = get_broken_links(".")
    for file, url in broken:
        print(f"Broken link: {url} (found in {file})")
    if broken:
        print(f"{len(broken)} broken link(s) found.")
        return 1
    print("No broken links found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
