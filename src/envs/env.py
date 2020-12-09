"""**Environment module commonly used in other files**

1. Signals are handled here
2. Set the printing options of `numpy` and `pandas`

-----
"""
### Import configs data
from configs.config import *


### Signal handling
from envs.SignalHandler import *
SignalHandler.register_sighandler(signal.SIGINT)


### Set the printing options
np.set_printoptions(suppress=True, precision=6, edgeitems=20, linewidth=1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', 1000)


### Remove warning (Glyps 8722)
plt.rc('axes', unicode_minus=False)
