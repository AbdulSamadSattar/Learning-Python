for i in range(5):
    a = (input("Enter Name :"))
    b = int(input("Enter Roll No. :"))
    c = (input("Enter Batch :"))
    d = (input("Enter Course :"))

    keys = {a.title()}
    value = [b,c,d]
    dict1 = dict.fromkeys(keys,value)
    print(dict1)
