#Make a script to find which number is greater than, less than, or equal
while True:
    a= int(input("Write any number: ",))
    if a < 10:
        print(a, "is smaller than 10")
    elif a == 10:
        print(a, "is equal to ten")
    elif a <= 25:
        print(a, " is equal or smaller than 25 but greater than 10 " )
    elif 50 > a:
        print(a, "is greater than 25 but smaller than 50")
    elif a == 50:
        print(a, "is equal to Fifty")
    else:
        print(a, "is greater than 50")
