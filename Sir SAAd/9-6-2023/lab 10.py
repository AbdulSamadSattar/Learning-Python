tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[2])
print ("tup2[1:5]: ", tup2[1:5])

#Create Single item in tuple
tup1 = (50)
print('\n\n',tup1)

tup1 = (50)
print (type(tup1))

tup1 = (50,)
print('\n\n',tup1)

tup1 = (50,)
print (type(tup1))

#Create a tuple from a list
tup4 = tuple([2 * x for x in range(1, 5)]) # (2, 4, 6, 8)
print('\n\n',tup4)