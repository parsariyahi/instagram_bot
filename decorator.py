import time
import json
from random import choice
def timer (func) :
    def wrraper (*args, **kwargs) :
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        run = end - start
        print(f'time : {run} -----')
    return wrraper
