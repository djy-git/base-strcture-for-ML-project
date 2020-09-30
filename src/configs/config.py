"""**Configuration variables are defined here**

1. Constants are CAPITAL letters
2. This file **should not** have functions or classes

----
"""
from envs.base_pkg import *
from configs.config_user import *


### Input, Output, Log directory
ROOT_DIR_PATH   = abspath(dirname(dirname(dirname(__file__))))
INPUT_DIR_PATH  = join(ROOT_DIR_PATH, "input")
OUTPUT_DIR_PATH = join(ROOT_DIR_PATH, "output")
LOG_DIR_PATH    = join(ROOT_DIR_PATH, "log")


### Random seed
SEED = 42
