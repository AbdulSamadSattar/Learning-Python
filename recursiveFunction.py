def print_numbers(n):
    if n > 10:      # Base case
        return
    print(n)
    print_numbers(n + 1)   # Recursive call

print_numbers(1)