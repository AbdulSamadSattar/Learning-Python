x = int(input("Enter an Integer: "))
def factorial(x):
    if x <=1 :
        return 1
    else:
        return x * factorial(x-1)

print(factorial(x))

    