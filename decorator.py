import time

def timer (func) :
    def wrraper (*args, **kwargs) :
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        run = end - start
        print(f'time : {run} -----')
        return value
    return wrraper


