from importlib.metadata import version

from .main import main

__all__ = ["main"]

__version__ = version("dso-mgr")
