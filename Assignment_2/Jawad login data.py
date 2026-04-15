def Create_New_Account():
    print("Create New Account")
    my_dic1=dict(User_Name=input("enter user name:"),Password=input("enter password:"))
    print("Account has been created")
    tuple1=tuple(my_dic1.values())
    print(tuple1)
    def Login_to_your_Account():
        print("Login to your account")
        my_dic2=dict(User_Name=input("enter user name:"),Password=input("enter password:"))
        tuple2=tuple(my_dic2.values())
        if tuple1==tuple2:
            print("\"you login to your account successfully\"")
        else:
             print("\"User_Name or Password is incorrect\"")
    print("do you want to login your account?")
    a=input("enter yes or no:")
    if a=="yes":
        Login_to_your_Account()
    elif a=="no":
        Create_New_Account()
    else:
        print("exit")
Create_New_Account()

   



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# print("Create New Account")   
# my_dic1=dict(User_Name=input("enter user name:"),Password=input("enter password:"))
# print("Account has been created")
# tuple1=tuple(my_dic1.items())
# print("Login to your account")
# my_dic2=dict(User_Name=input("enter user name:"),Password=input("enter password:"))
# tuple2=tuple(my_dic2.items())
# if tuple1==tuple2:
#     print("you login to your account successfully")
# else:
#     print("User_Name or Password is incorrect")

#to your account successfully")
# else:
#     print("User_Name or Password is incorrect")

    
        

































