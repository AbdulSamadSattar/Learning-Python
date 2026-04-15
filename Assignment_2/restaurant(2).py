import time
import pprint

# Menu dictionary with food items, waiting times, and prices
menu = {
    "Burger": {"waiting_time": 10, "price": 8.99},
    "Pizza": {"waiting_time": 15, "price": 12.99},
    "Pasta": {"waiting_time": 12, "price": 10.99},
    "Salad": {"waiting_time": 8, "price": 7.99},
    "Steak": {"waiting_time": 20, "price": 16.99},
    "Sushi": {"waiting_time": 18, "price": 14.99}
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
        time.sleep(waiting_time)  # Simulate waiting time
        print("Order ready!")
        print_receipt(food, waiting_time, price)
    else:
        print("Invalid food selection!")

def print_receipt(food, waiting_time, price):
    print("\nReceipt:")
    print("---------")
    print("Food:", food)
    print("Waiting Time:", waiting_time, "minutes")
    print("Price: $", price)
    print("Thank you for dining with us!")

# Main program
show_menu()
selected_food = input("Select a food item from the menu: ")
place_order(selected_food)
