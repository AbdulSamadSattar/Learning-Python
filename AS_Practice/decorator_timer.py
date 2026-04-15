import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Time:", end - start)
    return wrapper

@timer
def slow_function():
    for i in range(1000000):
        pass