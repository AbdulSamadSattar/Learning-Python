#2.1Make a script to find out whether the number is divisible by 2 or not.
while True:
    a = int(input("\n\tWrite any integer: "))
    if a % 2 == 0:
        print ( "The number is divisible by 2")
    else:
        print ("The number is not divisible by 2")
    restart = input("\n\t\tDo you want to restart the program? (yes/no): ")
    if restart.lower() == "no":
        break