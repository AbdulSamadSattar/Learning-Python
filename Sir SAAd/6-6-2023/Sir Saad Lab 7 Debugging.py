#Sir Saad Lab 7 Debugging
def sub(x, y):
    return x+y
print(sub(1,3))

def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " , animal_type ,".")
    print("My " , animal_type + "'s name is " , pet_name + ".")
describe_pet("Wade")

def type_of_int(i):
 if i % 2 == 0:
     print ('\neven')
 else:
     print('\nodd')
type_of_int(8)