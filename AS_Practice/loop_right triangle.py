size = 10
for i in range (size):
    count = size - i
    print('' * (count))
    print("*" * (i+1))
print("\n\n")
for i in range (size):
    count = size - i
    print('' * count)
    print("*" * (i+1))
print("\n\n")
for i in range (size):
    count = size - i
    print('' * i)
    print("*" * count)