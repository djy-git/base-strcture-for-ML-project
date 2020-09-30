"""Signal handler
1. Registered signal causes exit(1) with printing signal number
"""
from envs.base_env import *


class SignalHandler:
    @classmethod
    def register_sighandler(cls, signum):
        signal.signal(signum, cls.sighandler)

    @staticmethod
    def sighandler(signum, frame):
        print(f"Receive signal({signum})")
        exit(1)
