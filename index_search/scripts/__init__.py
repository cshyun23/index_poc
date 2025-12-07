"""
Package initializer for the index-search project.

On import this module will call src.config.init_paths() to resolve project paths
and ensure src/ is on sys.path so internal imports work when main.py or tests import src.
"""
from __future__ import annotations
import sys
import os
from typing import Optional

# lazy import to avoid circular import during packaging
try:
    from .config import init_paths, ProjectPaths, as_dict  # type: ignore
except Exception:
    # If config isn't available (e.g. during partial installs), define no-op placeholders
    def init_paths(root: Optional[str] = None, create_dirs: bool = True):
        return None
    ProjectPaths = None  # type: ignore
    def as_dict(x): return {}

_paths: Optional[ProjectPaths] = None

def ensure_paths(root: Optional[str] = None, create_dirs: bool = True) -> Optional[ProjectPaths]:
    """
    Initialize and return ProjectPaths. This will:
      - call src.config.init_paths(...)
      - add the src directory to sys.path (if not already present)
      - set module-level _paths for reuse

    Call ensure_paths() in scripts or import src then use src.paths
    """
    global _paths
    if _paths is not None:
        return _paths
    try:
        _paths = init_paths(root=root, create_dirs=create_dirs)
    except Exception:
        # If init_paths fails, leave _paths as None and don't crash imports
        _paths = None

    # Make sure src directory is importable (useful when running from project root)
    try:
        if _paths is not None:
            src_dir = str(_paths.src)
            if src_dir not in sys.path:
                sys.path.insert(0, src_dir)
            # also ensure project root is on sys.path
            root_dir = str(_paths.root)
            if root_dir not in sys.path:
                sys.path.insert(0, root_dir)
    except Exception:
        pass

    return _paths

# Initialize on import (safe-guarded)
paths = ensure_paths()

__all__ = ["ensure_paths", "paths", "init_paths", "ProjectPaths", "as_dict"]