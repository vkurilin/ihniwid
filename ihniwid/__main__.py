import sys

from ihniwid.backend import foo

if __name__ == "__main__":
    error_description = sys.argv[1]
    foo(error_description)
