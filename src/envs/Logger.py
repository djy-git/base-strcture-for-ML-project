"""**`Logger` logs the information of the process**

1. `Logger` logs the information at the log file as well as terminal
2. `Logger` assists fancy partitioning with 4 stages (chapter, section, subsection, subsubsection)

----
"""
from envs.env import *


class Logger:
    class LogOut:
        def __init__(self, log_dir_path):
            KST = timezone('Asia/Seoul')
            NOW = datetime.now(KST).strftime("%y-%m-%d(%H-%M-%S)")

            self.terminal = sys.stdout
            self.log = open(join(log_dir_path, f"{NOW}.log"), 'w')

        def write(self, msg):
            self.terminal.write(msg)
            self.log.write(msg)

        def flush(self):
            pass
    def __init__(self, log_dir_path):
        self.log_dir_path = log_dir_path

        self.num_chapter       = 0
        self.num_section       = 0
        self.num_subsection    = 0
        self.num_subsubsection = 0

        # Constant
        self.NUM_LOG_LENGTH = 80
    def change_stdout(self):
        sys.stdout = self.LogOut(self.log_dir_path)


    def info(self, *msgs):
        print(f">", *msgs)


    ### Log section
    def log_section(self, s):
        print(s[:self.NUM_LOG_LENGTH])
    def chapter(self, name):
        self.num_chapter += 1
        s = f"\n\n{'#'*10} Chapter {self.num_chapter} {name} {'#'*100}"
        self.log_section(s)
    def section(self, name):
        self.num_section += 1
        s = f"\n{'-'*4} Section {self.num_section} {name} {'-'*100}"
        self.log_section(s)
    def subsection(self, name):
        self.num_subsection += 1
        s = f"{'-'*4} Section {self.num_section}.{self.num_subsection} {name} {'-'*100}"
        self.log_section(s)
    def subsubsection(self, name):
        self.num_subsubsection += 1
        s = f"{'-'*4} Section {self.num_section}.{self.num_subsection}.{self.num_subsubsection} {name} {'-'*100}"
        self.log_section(s)


logger = Logger(LOG_DIR_PATH)
logger.change_stdout()


def chapter(fn):
    @timer
    @wraps(fn)
    def log(*args, **kwargs):
        logger.chapter(fn.__name__)
        rst = fn(*args, **kwargs)
        return rst
    return log
def section(fn):
    @timer
    @wraps(fn)
    def log(*args, **kwargs):
        logger.section(fn.__name__)
        rst = fn(*args, **kwargs)
        return rst
    return log
def subsection(fn):
    @timer
    @wraps(fn)
    def log(*args, **kwargs):
        logger.subsection(fn.__name__)
        rst = fn(*args, **kwargs)
        return rst
    return log
def subsubsection(fn):
    @timer
    @wraps(fn)
    def log(*args, **kwargs):
        logger.subsubsection(fn.__name__)
        rst = fn(*args, **kwargs)
        return rst
    return log
