"""**main module invoked in `setup.py`**

1. Usually, main module consists of switch statement for argument(command) from `setup.py`

----
"""
from envs.Logger import *


def log_sample():
    info("Do in log_sample")
    chapter1()
    chapter2()
@chapter
def chapter1():
    info("Do in chapter1")
    section1()
    section2()
@section
def section1():
    info("Do in section1")
    subsection1()
@section
def section2():
    info("Do in section2")
@subsection
def subsection1():
    info("Do subsection1")
@chapter
def chapter2():
    info("Do in chapter2")


if __name__ == "__main__":
    cmd = sys.argv[1]
    with Switch(cmd) as case:
        if case('run'):
            log_sample()

        if case('reset'):
            remove_dirs(G.INPUT_DIR_PATH, G.OUTPUT_DIR_PATH, G.LOG_DIR_PATH)

        if case.default:
            print(cmd, "is not valid value")
            raise ValueError
