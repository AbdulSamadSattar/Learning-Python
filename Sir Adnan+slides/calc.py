#Create a module calculator.py including two functions add and subtract taking two integer values as input and displ

def add():
    print("\tFor Addition")
    a = int(input("Enter 1st Integer Value : "))
    b = int(input("Enter 2nd Integer Value : "))
    c = a + b
    print("Addition of",a,"&",b,"=",c)
    
def subtract():
    print("\n\tFor Subtraction")
    d = int(input("Enter 1st Integer Value : "))
    e = int(input("Enter 2nd Integer Value : "))
    f = d - e
    print("Subtraction of",d,"&",e,"=",f)
    
def multiply():
    print("\n\tFor Multiplication")
    s = int(input("Enter 1st Integer Value : "))
    t = int(input("Enter 2nd Integer Value : "))
    u = s * t
    print("Multiplication of",s,"&",t,"=",u)
    
def divide():
    print("\n\tFor Division")
    x = int(input("Enter 1st Integer Value : "))
    y = int(input("Enter 2nd Integer Value : "))
    z = x / y
    print("Division of",x,"&",y,"=",z)