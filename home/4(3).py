#Make a script to find which number is greater than, less than, or equal
print("\t\t\tEnter a=0,b=0 to end a program")
while True:
    print("\nEnter two numbers to find which is greater, less than, or equal")
    a= int(input("Write 1st number: ",))
    b= int(input("Write 2nd number: ",))
    if a < b:
        print(a, "is smaller than", b)
    elif (a,b) == (0,0):
        break 
    elif a == b:
        print(a, "is equal to", b)  
    else:
        print(a, " is greater than", b)