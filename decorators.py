def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


'''
@my_decorator
def greet():
    print("Hello")

    Equivalent to

def greet():
    print("Hello")

greet = my_decorator(greet)

'''

@my_decorator
def greet():
    print("Hello")
    
greet()