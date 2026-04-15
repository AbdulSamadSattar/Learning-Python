#Make a script to develop a simple calculator.
while True:
    c=input("\n\tSelect an operator(+,-,*,/): ")
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    if c == '+':
        print(a,"+",b, "=", a+b)
    elif c == "-":
        print(a,"-",b, "=", a-b)
    elif c == '*':
        print(a,"*",b, "=", a*b)
    elif c == '/':
        print(a,"/",b, "=", a/b)
    else:
        print(a,"+",b, "=", a+b)
        print(a,"-",b, "=", a-b)
        print(a,"*",b, "=", a*b)
        print(a,"/",b, "=", a/b)