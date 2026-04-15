import random
import time
import pprint

# Menu dictionary with food items and their waiting times
menu = {
    "Burger": 10,
    "Pizza": 15,
    "Pasta": 12,
    "Salad": 8,
    "Steak": 20,
    "Sushi": 18
}

def show_menu():
    print("Welcome to the Restaurant!")
    print("Menu Card:")
    pprint.pprint(menu)

def place_order(food):
    if food in menu:
        print(f"Selected food: {food}")
        waiting_time = menu[food]
        print(f"Waiting time for {food}: {waiting_time} minutes")
        print("Preparing your order...")
        time.sleep(waiting_time)  # Simulate waiting time
        print("Order ready!")
        print_receipt(food, waiting_time)
    else:
        print("Invalid food selection!")

def print_receipt(food, waiting_time):
    print("\nReceipt:")
    print("---------")
    print("Food:", food)
    print("Waiting Time:", waiting_time, "minutes")
    print("Total Amount: $", random.randint(10, 50))
    print("Thank you for dining with us!")

# Main program
show_menu()
selected_food = input("Select a food item from the menu: ")
place_order(selected_food)
