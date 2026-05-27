from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))


def test_package_imports():
    import moving_detection

    assert moving_detection.__all__ == []
