from envs.base_env import *


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

        self.space = 0

    def get_stdout(self):
        print("")
        return self.LogOut(self.log_dir_path)

    def info(self, *msgs):
        if self.num_section == 0:
            print(f"{' '*self.space}>", *msgs)
        else:
            print(f"{' '*(self.space+2)}>", *msgs)

    def chapter(self, *msgs):
        self.num_chapter += 1
        self.space = 0
        print(f"{' '*self.space}Chapter {self.num_chapter}", *msgs)

    def section(self, *msgs):
        self.num_section += 1
        self.space = 0
        print(f"{' '*self.space}{self.num_section}", *msgs)

    def subsection(self, *msgs):
        self.num_subsection += 1
        self.space = 2
        print(f"{' '*self.space}{self.num_section}.{self.num_subsection}", *msgs)

    def subsubsection(self, *msgs):
        self.num_subsubsection += 1
        self.space = 4
        print(f"{' '*self.space}{self.num_section}.{self.num_subsection}.{self.num_subsubsection}", *msgs)
