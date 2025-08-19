import os
import sys

# Ensure the repository root is on the Python path so that the
# `scripts` package can be imported when tests are executed via pytest
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.check_links import check_links


def test_links_are_valid():
    result = check_links()
    assert not result['failed'], f"Broken links found:\n" + "\n".join(
        f"{r.source}: {r.url} -> {r.status}" for r in result['failed']
    )
