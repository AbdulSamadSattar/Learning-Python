#a = input("Write City Name:")
def describe_city(a,y="Paksitan"):
    #a = input("Write City Name:")
    print(a, "is in",y)
    
describe_city('karachi')
describe_city('Lahore')
describe_city('Riyadh','Saudia Arab')



def make_pizza(size,*toppings):
    print("\nMake a pizza of size",size,"\'\' with following topics")
    print(toppings)
    
make_pizza(8,'extra cheese')
make_pizza(12,'mushroom','olive','black pepper')