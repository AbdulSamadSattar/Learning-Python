import random

def temperature():
    lst1 = []
    
    for i in range (30):
        temp = random.randrange(5,31)
        lst1.append(temp)
        
    total = 0
    for x in lst1:
        total += x
    avg = total/30
    
    print(lst1)
    print("Average temp of a month is", avg)
    print("Maximum temp in a Month is", max(lst1))
    print("Minimum temp in a Month is", min(lst1))
    
temperature()