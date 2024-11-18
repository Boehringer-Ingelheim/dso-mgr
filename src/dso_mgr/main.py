#!/usr/bin/env python3
try:
    import tomllib
except ImportError:
    # for compatibility with python < 3.11
    import tomli as tomllib
from pathlib import Path
from subprocess import run
from sys import argv


def _within_dso_project(path: Path) -> bool:
    """Determine whether or not we are inside a dso project.

    Being within a dso project is defined by the presence of a `pyproject.toml` file in any parent directory
    which has a `[tool.dso]` entry with flag `use_dso_mgr` set to True.
    """
    if path == Path("/"):
        return False

    pyproject_toml_file = path / "pyproject.toml"
    if pyproject_toml_file.exists():
        with pyproject_toml_file.open("rb") as f:
            pyproject_toml = tomllib.load(f)
            dso_cfg = pyproject_toml.get("tool", {}).get("dso", {})
            # otherwise keep recursing, there might be another pyproject.toml that's relevant
            if dso_cfg.get("use_dso_mgr", False):
                return True

    return _within_dso_project(path.parent)


def main():
    """Wrapper for calling dso from dso-core

    When within a dso project, execute the dso version that's specified in that project's pyproject.toml.
    Otherwise execute the latest version that's available from PyPI (uv's caching rules apply).
    """
    if _within_dso_project(Path.cwd()):
        run(["uv", "run", "--", "dso", *argv[1:]])
    else:
        run(["uv", "tool", "run", "--from", "dso-core", "dso", *argv[1:]])


if __name__ == "__main__":
    main()
