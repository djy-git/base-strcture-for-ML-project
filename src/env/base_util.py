from env.base_env import *


def generate_dirs(*dirs):
    print("> Generate directories")
    for dir in dirs:
        try:
            os.makedirs(dir)
            print(f"Generate directory: '{dir}'")
        except:
            print(f"Existing directory: '{dir}'")
