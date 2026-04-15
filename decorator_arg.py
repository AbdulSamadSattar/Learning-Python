# Normal decorator only works with functions without parameters.
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
        print("After")
    return wrapper

@my_decorator
def add(a, b):
    print(a + b)

add(3, 4)