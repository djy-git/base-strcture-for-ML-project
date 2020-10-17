"""**main module invoked in `setup.py`**

1. Usually, main module consists of switch statement for argument(command) from `setup.py`

----
"""
from envs.env import *


def log_sample():
    print("Do in log_sample")
    chapter1()
    chapter2()

@chapter
def chapter1():
    print("Do in chapter1")

    section1()
    section2()

@section
def section1():
    print("Do in section1")

    subsection1()

@section
def section2():
    print("Do in section2")

@subsection
def subsection1():
    print("Do subsection1")

@chapter
def chapter2():
    print("Do in chapter2")




if __name__ == "__main__":
    cmd = 'log_sample'  # sys.argv[1]
    with Switch(cmd) as case:
        if case('log_sample'):
            log_sample()

        if case('reset'):
            remove_dirs(INPUT_DIR_PATH, OUTPUT_DIR_PATH, LOG_DIR_PATH)

        if case.default:
            raise ValueError
