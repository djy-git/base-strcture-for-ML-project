from envs.env import *


def log():
    logger.chapter("happy", "halloween")
    logger.info("A", "B", "C")

    logger.section("happy", "halloween")
    logger.info("A", "B", "C")

    logger.subsection("happy", "halloween")
    logger.info("A", "B", "C")

    logger.subsubsection("happy", "halloween")
    logger.info("A", "B", "C")


if __name__ == "__main__":
    cmd = sys.argv[1]
    with Switch(cmd) as case:
        if case('log'):
            log()

        if case('reset'):
            remove_dirs(INPUT_DIR_PATH, OUTPUT_DIR_PATH, LOG_DIR_PATH)

        if case.default:
            raise ValueError
