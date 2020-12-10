"""**Utility module**

1. This file defines commonly used functions or classes
2. This has the highest dependency level in envs.
   Thus, just import this module instead of other modules.

----
"""
from envs.env import *


### Log utility function
info = lambda *msgs: print(f">", *msgs)


### Control directories
def generate_dirs(*dirs):
    info("Generate directories")
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


### Wrapper function
def timer(fn):
    @wraps(fn)
    def log(*args, **kwargs):
        start_time = time()
        rst = fn(*args, **kwargs)
        elapsed_time = time() - start_time
        G.total_time += elapsed_time
        print(f"[{fn.__name__}] {elapsed_time:.1f}s (total: {G.total_time:.1f}s)")
        return rst
    return log
def meminfo(fn):
    def log_gpu_memory():
        print(f"\n{'='*100}")
        for idx_gpu in range(len(cuda.gpus)):
            current_context = cuda.current_context()
            memories = current_context.get_memory_info()
            gpu_memory = dict(free=f"{memories.free // 2 ** 20} MB",
                              total=f"{memories.total // 2 ** 20} MB")
            print(f'------------------- GPU {idx_gpu} MEMORY:', gpu_memory, '-------------------')
        print(f"\n{'='*100}")

    @wraps(fn)
    def log(*args, **kwargs):
        log_gpu_memory()
        rst = fn(*args, **kwargs)
        log_gpu_memory()
        return rst
    return log


### Debugging line logger
###     Usage: log_line(currentframe())
def log_line(cur_frame):
    frameinfo = getframeinfo(cur_frame)
    filename = frameinfo.filename.split('/')[-1]
    print(f"\n** log_line(): {filename} (line {frameinfo.lineno}) ** \n")
