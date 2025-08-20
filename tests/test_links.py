import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from scripts.check_links import get_broken_links


def test_no_broken_links():
    broken = get_broken_links(".")
    assert not broken, "Broken links found:\n" + "\n".join(
        f"{url} (in {file})" for file, url in broken
    )
