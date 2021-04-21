import gc
import traceback
from types import FunctionType
from itertools import islice

from IPython.core.magic import Magics, magics_class, line_magic
from IPython.display import display

from .utils import last
from .captcha import CaptchaError
from .backend import find_code_suggestions

__all__ = ('MyMagics',)


@magics_class
class MyMagics(Magics):
    def __init__(self, shell):
        super().__init__(shell)
        self.last_exc_info = None

    @line_magic
    def ihniwid(self, line):
        # Determine the search term.
        if line:
            term = line
        else:
            term = self.build_term_from_last_exception()
            if not term:
                print('No exception has been thrown yet!')
                print('Tip: you can specify a search term explicitly.')
                return None

        # Do search.
        for suggestion in islice(find_code_suggestions(term), 10):
            display(suggestion)


    def build_term_from_last_exception(self):
        try:
            exc_type, exc_value, tb = self.shell._get_exc_info()
        except ValueError:
            return None
        # If the last exception is our own CaptchaError, supress that and
        # the previous one we have saved.
        if exc_type is CaptchaError:
            if self.last_exc_info is None:
                return None
            exc_type, exc_value, tb = self.last_exc_info
        else:
            self.last_exc_info = exc_type, exc_value, tb

        # Take at most 7 words from the exception description.
        message = ' '.join(islice(str(exc_value).split(), 7))
        print('message is', message)
        term = exc_type.__name__ + ': ' + message
        # Prepend the module name, if any.
        last_frame, lineno = last(traceback.walk_tb(tb))
        nearest_module_name = self.find_module_name(last_frame.f_code)
        if nearest_module_name:
            term = f'{nearest_module_name}: {term}'
        return term

    @staticmethod
    def find_module_name(code):
        """Find the name of the module a code object been defined in.

        This method uses some arcane dark magic to accomplish this.
        Do not try this at home.
        """
        # First, look for a function that references this code object.
        functions = (
            function for function in gc.get_referrers(code)
            if isinstance(function, FunctionType)
            and getattr(function, '__code__') is code
        )
        function = next(functions, None)
        if function is None:
            return None
        # Now, we can just fetch the module name from the function.
        return function.__module__

