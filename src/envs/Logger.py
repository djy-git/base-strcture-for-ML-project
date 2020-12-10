"""**`Logger` logs the information of the process**

1. `Logger` logs the information at the log file as well as terminal
2. `Logger` assists fancy partitioning with 4 stages (chapter, section, subsection, subsubsection)

----
"""
from envs.util import *


class Logger:
    class LogOut:
        def __init__(self, log_dir_path):
            generate_dirs(log_dir_path)
            KST = timezone('Asia/Seoul')
            NOW = datetime.now(KST).strftime("%y-%m-%d_%H-%M-%S")

            self.terminal = sys.stdout
            self.logger   = open(join(log_dir_path, f"{NOW}.log"), 'w')
        def __del__(self):
            self.logger.close()

        def flush(self): pass
        def write(self, msg):
            self.terminal.write(msg)
            self.logger.write(msg)

    def __init__(self, log_dir_path):
        self.log_dir_path = log_dir_path

        self.num_chapter       = 0
        self.num_section       = 0
        self.num_subsection    = 0
        self.num_subsubsection = 0

        ### Constant
        self.NUM_LOG_LENGTH = 80

        self.change_stdout()
    def change_stdout(self):
        sys.stdout = self.LogOut(self.log_dir_path)

    ### Log section
    def log(self, s):
        print(s[:self.NUM_LOG_LENGTH])
    def chapter(self, name):
        self.num_chapter += 1
        self.num_section = self.num_subsection = self.num_subsubsection = 0
        s = f"\n\n{'#'*10} Chapter {self.num_chapter} {name} {'#'*100}"
        self.log(s)
    def section(self, name):
        self.num_section += 1
        self.num_subsection = self.num_subsubsection = 0
        s = f"{'-' * 4} Section {self.num_section} {name} {'-' * 100}"
        if self.num_section > 1:
            s = "\n" + s
        self.log(s)
    def subsection(self, name):
        self.num_subsection += 1
        self.num_subsubsection = 0
        s = f"{'-'*4} Section {self.num_section}.{self.num_subsection} {name} {'-'*100}"
        self.log(s)
    def subsubsection(self, name):
        self.num_subsubsection += 1
        s = f"{'-'*4} Section {self.num_section}.{self.num_subsection}.{self.num_subsubsection} {name} {'-'*100}"
        self.log(s)


logger = Logger(G.LOG_DIR_PATH)


### Wrapper
def chapter(fn):
    @timer
    @wraps(fn)
    def log(*args, **kwargs):
        logger.chapter(fn.__name__)
        rst = fn(*args, **kwargs)
        return rst
    return log
def section(fn):
    @wraps(fn)
    def log(*args, **kwargs):
        logger.section(fn.__name__)
        rst = fn(*args, **kwargs)
        return rst
    return log
def subsection(fn):
    @wraps(fn)
    def log(*args, **kwargs):
        logger.subsection(fn.__name__)
        rst = fn(*args, **kwargs)
        return rst
    return log
def subsubsection(fn):
    @wraps(fn)
    def log(*args, **kwargs):
        logger.subsubsection(fn.__name__)
        rst = fn(*args, **kwargs)
        return rst
    return log
