from envs.base_env import *
from configs.config_user import *


### Input, Output, Log directory
ROOT_DIR_PATH   = dirname(dirname(dirname(__file__)))
INPUT_DIR_PATH  = join(ROOT_DIR_PATH, "input")
OUTPUT_DIR_PATH = join(ROOT_DIR_PATH, "output")
LOG_DIR_PATH    = join(ROOT_DIR_PATH, "log")
