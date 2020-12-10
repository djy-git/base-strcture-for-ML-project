"""**Base package module**

1. This file **should not** import other modules or packages in the project (thus, **base**)
2. This file only imports commonly used packages

----
"""
### Internal packages
import os
from os.path import join, isdir, dirname, basename, abspath
import shutil
import sys
from time import time, sleep
from datetime import datetime
from pytz import timezone
from abc import ABCMeta, abstractmethod
import signal
from functools import wraps
from inspect import currentframe, getframeinfo


### External packages
import numpy as np
import pandas as pd
from tabulate import tabulate
from tqdm import tqdm
from switch import Switch


### Plotting packages
import matplotlib.pyplot as plt
import sns


### Parallelization packages
import numba as nb
from dask import delayed, compute


### CUDA
from numba import cuda, int16, float32
