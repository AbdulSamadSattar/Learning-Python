def create_account():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    print('Your Username is:', username.title())
    print('Your Password is:', password)
    account = ((username, password))
    print(account)
    return account

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return (username.title(), password)

def admin_login():
    accounts = ()
    
    while True:
        print("\n--- Admin Login System ---")
        print("1. Create Account")
        print("2. Log In")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            print('Create Account')
            print (accounts)
            a=list(accounts)
            print (a)
            account = create_account()
            a.append(account)
            print(a)
            accounts=((a))
            print(accounts)
            print("Account created successfully.")
        elif choice == "2":
            print('Log In')
            user_login = login()
            if user_login in accounts:
                print("Login successful.")
            else:
                print("Invalid username or password. Please try again.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-3).")

admin_login()
