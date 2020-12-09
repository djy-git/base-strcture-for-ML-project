"""**Configuration variables are defined here**

1. All global variables are attributes in class G
2. Constants are CAPITAL letters

----
"""
from envs.base_env import *
from configs.config_user import *


class G:
    ### Input, Output, Log directory
    ROOT_DIR_PATH   = abspath(dirname(dirname(dirname(__file__))))
    INPUT_DIR_PATH  = join(ROOT_DIR_PATH, "input")
    OUTPUT_DIR_PATH = join(ROOT_DIR_PATH, "output")
    LOG_DIR_PATH    = join(ROOT_DIR_PATH, "log")


    ### Random seed
    SEED = 42


    ### Total elapsed time
    total_time = 0
