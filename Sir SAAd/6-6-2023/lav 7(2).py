#Write a function called max( ), that returns the maxium of three integer numbers.
def max(x,y,z):
    if x > y > z or x>z>y:
        print (x)
    elif y >z > x or y >x>z:
        print (y)
    else:
        print (z)
max(3,200,10)