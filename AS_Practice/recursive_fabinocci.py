def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

shown_once = False  # Python has no 'static' keyword; a flag does the same job

print("Welcome! Enter a positive integer for Fibonacci.")
print("Press 'n' anytime to stop.")

while True:
    user_input = input("Enter input: ").lower()  # real .lower() method

    if user_input == "n":
        print("Program stopped.")
        break

    try:
        a = int(user_input)   # typecasting string -> int
    except ValueError:
        print("Invalid input. Please enter a number or 'n' to stop.")
        continue

    if a < 0:
        print("Please enter a positive integer.")
        continue

    print(f"Fibonacci at position {a} is {fib(a)}")