from concurrent.futures.process import _ThreadWakeup
from importlib.resources import is_resource
from tkinter import Menu


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"sorry there is no enough {item}")
            return False
    return True


def process_coins():
    print("Please insert the coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit+= drink_cost
        return True
    else:
        print("insuffucient money, money refunded")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")

        




profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_onn=True
while is_onn:
    choice= input("What would you like to have? epresso, cappucino,latte?").lower()
    if choice=='off':
        is_onn=False
    elif choice=='report':
        print(f"Water: {resources['water']} ml.")
        print(f"Milk: {resources['milk']} ml.")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment= process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])









       
