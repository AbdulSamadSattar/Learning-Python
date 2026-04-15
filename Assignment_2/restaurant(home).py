import pprint
# Menu dictionary with food items, waiting times, and prices
menu = {
    "Burger": {"waiting_time": 5, "price": 650},
    "Pizza": {"waiting_time": 12, "price": 1800},
    "Tikka": {"waiting_time": 15, "price": 500},
    "Biryani": {"waiting_time": 10, "price": 1200},
    "Ice-cream": {"waiting_time": 2, "price": 450},
}

def show_menu():
    print("Welcome to the Restaurant!")
    print("Menu Card:")
    pprint.pprint(menu)

def place_order(food):
    if food in menu:
        print(f"Selected food: {food}")
        waiting_time = menu[food]["waiting_time"]
        price = menu[food]["price"]
        print(f"Waiting time for {food}: {waiting_time} minutes")
        print("Preparing your order...")
       
        print("Order ready!")
        print_receipt(food, waiting_time, price)
    else:
        print("Invalid food selection!")

def print_receipt(food, waiting_time, price):
    print("\nReceipt:")
    print("---------")
    print("Food:", food)
    print("Waiting Time:", waiting_time, "minutes")
    print("Price: Rs", price)
    print("Thank you for dining with us!")

# Main program
show_menu()
selected_food = input("Select a food item from the menu: ")
place_order(selected_food.capitalize())

