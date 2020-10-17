"""**main module invoked in `setup.py`**

1. Usually, main module consists of switch statement for argument(command) from `setup.py`

----
"""
from envs.env import *


def log_sample():
    """
    Log sample
    """
    logger.chapter("happy", "halloween")
    logger.info("A", "B", "C")

    logger.section("happy", "halloween")
    logger.info("A", "B", "C")

    logger.subsection("happy", "halloween")
    logger.info("A", "B", "C")

    logger.subsubsection("happy", "halloween")
    logger.info("A", "B", "C")


if __name__ == "__main__":
    logger = Logger(LOG_DIR_PATH)
    logger.change_stdout()

    cmd = 'log'  # sys.argv[1]
    with Switch(cmd) as case:
        if case('log'):
            log_sample()

        if case('reset'):
            remove_dirs(INPUT_DIR_PATH, OUTPUT_DIR_PATH, LOG_DIR_PATH)

        if case.default:
            raise ValueError
