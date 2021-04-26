"""A simple tool that will try to find answers on stackoverflow for you."""
import gettext
from pathlib import Path

from .magic import MyMagics

path_to_locale_dir = Path(__path__[0]) / "locale"  # type: ignore # noqa
gettext.install("ihniwid", path_to_locale_dir)

__all__ = ("load_ipython_extension",)


def load_ipython_extension(ipython):
    """Load this extension into IPython.

    This is the function IPython looks for when you import an extension
    with `%load_ext ihniwid`.
    """
    ipython.register_magics(MyMagics)
