from pprint import pformat
from inspect import getargspec

class Debug(object):
    """Decorator for debugging functions.

    This decorator is used to debug a function, or
    a class method. If this is applied to a normal
    function, it will print out the arguments of

    Keyword arguments:
    debug -- Whether or not you want to output debug info.
    """
    def __init__(self, debug=True):
        self.debug = debug

    def __format_debug_string(self, function, *args, **kwargs):
        """Return a formatted debug string.

        This is a small private helper function that will
        return a string value with certain debug information.

        Keyword arguments:
        function -- The function to debug.
        *args    -- The normal arguments of the function.
        **kwargs -- The keyword arguments of the function.
        """
        debug_string = ""
        debug_string += "[debug] {}\n".format(pformat(function))
        debug_string += "[debug] Passed args: {}\n".format(pformat(args))
        debug_string += "[debug] Passed kwargs: {}\n".format(pformat(kwargs))
        debug_string += "[debug] Locals: {}".format(pformat(function.__code__.co_varnames))
        return debug_string

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            if self.debug:
                if getargspec(function).args[0] != "self":
                    print(self.__format_debug_string(function, *args, **kwargs))
                else:
                    print(self.__format_debug_string(function, *args, **kwargs))
                    print("[debug] Parent attributes: {}".format(pformat(args[0].__dict__)))

            return function(*args, **kwargs)
        return wrapper
