"""**Base utility module**

1. This file **should not** import other modules or packages in the project except `base_pkg.py` (thus, **base**)
2. This file only defines commonly used functions or classes

----
"""
from envs.base_pkg import *


### Control directories
def generate_dirs(*dirs):
    print("> Generate directories")
    for dir in dirs:
        try:
            os.makedirs(dir)
            print(f"Generate directory: '{dir}'")
        except:
            print(f"Existing directory: '{dir}'")
def remove_dirs(*dirs):
    print("> Remove directories")
    for dir in dirs:
        try:
            os.removedirs(dir)
            print(f"Remove empty directory: '{dir}'")
        except:
            shutil.rmtree(dir)
            print(f"Remove not empty directory: '{dir}'")
