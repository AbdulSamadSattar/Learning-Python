numbers = [2, 5, 2, 7, 5, 9, 7]
unique_list = []

for number in numbers:
    if number not in unique_list:
        unique_list.append(number)

for number in unique_list:
    print(number)