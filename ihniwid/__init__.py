import gettext

from .magic import MyMagics

gettext.install("ihniwid", "locale")

__all__ = ("load_ipython_extension",)


def load_ipython_extension(ipython):
    """Load this extension into IPython.

    This is the function IPython looks for when you import an extension
    with `%load_ext ihniwid`.
    """
    ipython.register_magics(MyMagics)
