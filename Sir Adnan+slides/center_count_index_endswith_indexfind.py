a = 'onlystring'
print('a.center(13,\'9\') =',a.center(13,'9'))
print(a*3)
search = 'n'
print('Count = ',a.count(search,-2,-1))

var = 'programming'
print(var[3:-3])
print('programming [3:-3]=',var.endswith('a',-9,-5))

var = 'Hello World'
a = 'w'
print('w in hello World(-8,-4)= ',var.endswith(a.capitalize(),-8,-4))

str1 = 'This is STRing'
str2 = 'str'
print('find:\'This is STRing\': ',str1.find(str2.upper(),2,20))
print('index:\'This is STRing\': ',str1.index(str2.upper(),2,15))
