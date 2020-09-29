"""Signal handling
1. Registered signal causes exit(1) with printing signal number
"""
from base_env import *


def sighandler(signum, frame):
    print(f"Receive signal({signum})")
    exit(1)


def register_sighandler(signum):
    signal.signal(signum, sighandler)
