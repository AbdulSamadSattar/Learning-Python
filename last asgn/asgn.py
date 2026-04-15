# Sample user data (for demonstration purposes)
users = {
    "admin": "admin123",
    "student1": "student11",
    "student2": "student22"
}

# Sample marks data (student, subject, marks)
marks_data = {
    "student1": {
        "Math": 85,
        "Science": 78,
        "History": 92
    },
    "student2": {
        "Math": 70,
        "Science": 85,
        "History": 60
    }
}

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        return username
    else:
        return None

def enter_marks(username):
    if username == "admin":
        student = input("Enter student's username: ")
        if student in marks_data:
            for subject in marks_data[student]:
                marks = int(input(f"Enter marks for {subject}: "))
                marks_data[student][subject] = marks
            print("Marks entered successfully.")
        else:
            print("Student not found.")
    else:
        print("Access denied. Only admin can enter marks.")

def view_marks(username):
    if username in marks_data:
        print("Your Marks:")
        for subject, marks in marks_data[username].items():
            print(f"{subject}: {marks}")
    else:
        print("Marks not available.")

def main():
    while True:
        print("\nWelcome to the Student Portal")
        print("1. Login")
        print("2. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            username = login()
            if username:
                print(f"Welcome, {username}!")
                while True:
                    print("\n1. Enter Marks (Admin)")
                    print("2. View Marks (Student)")
                    print("3. Logout")
                    option = input("Select an option: ")

                    if option == "1":
                        enter_marks(username)
                    elif option == "2":
                        view_marks(username)
                    elif option == "3":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option.")
            else:
                print("Invalid username or password.")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
