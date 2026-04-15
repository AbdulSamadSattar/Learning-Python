students = {"111-29":"Sarmad","111-30":"Jawad","111-31":"John", "111-32":"Peter"}
z= students.keys()
print(z,'\n')

y=students.values()
print(y,'\n')

x=students.items()
print(x,'\n')

print(students.get('111-30'),'\n')


print(students.popitem(),'\n')#Always show the last one


print(students.clear(),'\n')

my_dict = {'a': 1, 'b': 2, 'c': 3}
m = my_dict.keys()
for i in m:
    print(m)
    
my_dict1 = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict1.keys()
for key in keys:
    print(key)
    
dict_items=([('111-29', 'Sarmad'), ('111-30', 'Jawad'), ('111-31', 'John'), ('111-32', 'Peter')]) 
print('\n\t\t',dict_items[2][1])