"""**Utility module**

1. This file defines commonly used functions or classes
2. This has the highest dependency level in envs.
   Thus, just import this module instead of other modules.

----
"""
from envs.env import *


### Control directories
def generate_dirs(*dirs):
    print("> Generate directories")
    for dir in dirs:
        try:
            os.makedirs(dir)
            print(f"Generate directory: '{dir}'")
        except:
            pass
            # print(f"Existing directory: '{dir}'")
def remove_dirs(*dirs):
    print("> Remove directories")
    for dir in dirs:
        try:
            os.removedirs(dir)
            print(f"Remove empty directory: '{dir}'")
        except:
            shutil.rmtree(dir)
            print(f"Remove not empty directory: '{dir}'")


### Wrapper function
def timer(fn):
    @wraps(fn)
    def log(*args, **kwargs):
        start_time = time()
        rst = fn(*args, **kwargs)
        elapsed_time = time() - start_time
        print(f"[Elapsed time - {fn.__name__}] {elapsed_time:.1f}s")
        return rst
    return log


def info(*msgs):
    print(f">", *msgs)
