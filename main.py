"""
Example main that uses src package initializer. Run from project root:
  python -m src.main
"""
from __future__ import annotations
import sys
# import the package to trigger init
import src

def main():
    # paths was initialized on import; ensure it's available
    paths = getattr(src, "paths", None)
    if not paths:
        # fallback: explicitly initialize (useful in some test runners)
        paths = src.ensure_paths()
    print("Project root:", paths.root if paths else "unknown")
    print("Src path:", paths.src if paths else "unknown")
    # ... continue with app startup ...

if __name__ == "__main__":
    main()