def gpa():
    print("1st semester")
    a = int(input('Enter marks of CS101:'))
    a1 = int(input('Enter credit hours of CS101:'))
    b = int(input('Enter marks of Eng 101:'))
    b1 = int(input('Enter credit hours of Eng 101:'))
    c = int(input('Enter marks of Pak 301:'))
    c1 = int(input('Enter credit hours of Pak 301:'))
#     d = int(input('Enter marks of Isl 201:'))
#     d1 = int(input('Enter credit hours of Isl 201:'))
#     e = int(input('Enter marks of Phy 101:'))
#     e1 = int(input('Enter credit hours of Phy 101:'))
#     f = int(input('Enter marks of Mth 101:'))
#     f1 = int(input('Enter credit hours of Mth 101:'))
    
    res = a/25*a1 + b/25*b1 + c/25*c1 #+ d/25*d1 + e/25*e1 +f/25 *f1
    total = print('GPA=',res/(a1+b1+c1))#+d1+e1+f1))						 #remove ))

    
    
    
    
    
    
    
    
    
    