import functools
import time

def boilerplate(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        print("Testing decorator...")
        value = func(*args, **kwargs)
        # Do something after
        print("Decorator works!")
        return value
    return wrapper_decorator

def benchmark(func):
    @functools.wraps(func)
    def wrapper(*args: any, **kwargs: any):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        total = end - start
        print(f"Function {func.__name__} executed in {total:.4f} secs")
        return value
    return wrapper