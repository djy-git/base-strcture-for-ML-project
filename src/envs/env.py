"""**Environment module commonly used in other files**

1. This file imports `base_util.py` for base packages and base functions or classes
2. Signals are handled here
3. Generate input, output, log directories in `ROOT_DIR_PATH` defined in `config.py`
4. Import Logger
5. Set the printing options of `numpy` and `pandas`

-----
"""
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


### Set the printing options
np.set_printoptions(suppress=True, precision=6, edgeitems=20, linewidth=1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', 1000)


### Remove warning (Glyps 8722)
plt.rc('axes', unicode_minus=False)
