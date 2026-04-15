student_info = []
def sign_up():
    print("Create your account")
#     a = input("Enter your User Name:")
    b = input("Enter your Email:")
#     c = int(input("Enter your Number:"))
    d = input("Enter your Password: ")
    student_info.append((b,d))
    print(student_info)
    
def log_in():
    print("Log in")
    e = input("Enter your Email or Phone number:")
    f = input("Password: ")
    if (e,f) in student_info:
        print("Log in Successful ")
    else:
        print("Invalid Email id or Password")
while 1:
    print("Choose any one option")
    print("For sign-up : 1")
    print("For log-in : 2")
    print("For Exit : 3")
    g = input("Enter any one of the above option: ")


    if g == '1':
        sign_up()
    elif g == '2':
        log_in()
    elif g == '3':
        print("Existing")
        break
    else:
        print("invalid choice")
    
        
