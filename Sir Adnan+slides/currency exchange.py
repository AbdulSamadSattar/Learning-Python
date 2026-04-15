import math
while 1:
    print("\n\tPress")
    print(' \'P\' for UK Pound Conversion: (1P = 360 Pkr) ')
    print(' \'D\' for US Dollar Conversion: (1D = 285 Pkr) ')
    print(' \'R\' for Saudi Riyal Conversion: (1R = 76 Pkr) ')
    choice = input("Enter your choice:")

    def pound():
        a = int(input("Enter Pakistani Rupee:"))
        res1 = a / 360
        print(a,"Pkr =",round(res1,2),"pounds(approx)")
    def dollar():
        a = int(input("Enter Pakistani Rupee:"))
        res2 = a / 285
        print(a,"Pkr =",round(res2,2),"$(approx)")
    def riyal():
        a = int(input("Enter Pakistani Rupee:"))
        res3 = a / 76
        print(a,"Pkr =",round(res3,2),"Riyal(approx)")
        
    if choice.capitalize() == 'P':
        pound()
    elif choice.capitalize() == 'D':
        dollar()
    elif choice.capitalize() == 'R':
        riyal()
    else:
        print('Wrong Choice')
