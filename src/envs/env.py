### Import base library
from envs.base_util import *


### Import configs data
from configs.config import *


### Signal handling
from envs.SignalHandler import *
SignalHandler.register_sighandler(signal.SIGINT)


### Make directories
generate_dirs(INPUT_DIR_PATH, OUTPUT_DIR_PATH, LOG_DIR_PATH)


### Logger
from envs.Logger import *
logger     = Logger(LOG_DIR_PATH)
sys.stdout = logger.get_stdout()


### Set environment
np.set_printoptions(suppress=True, precision=6, edgeitems=20, linewidth=1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', 1000)
