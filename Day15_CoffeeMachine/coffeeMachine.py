import os

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coffeeMachine():
    os.system('cls')
    global profit
    print(profit)

    #return lacking resources or True if the item can be made
    def checkResources(item):
        for res in MENU[item]["ingredients"]:
            if MENU[item]["ingredients"][res] >= resources[res]:
                print(f"Sorry, there is not enough {res}")
                return False
        return True

    #process the transaction, deduct resources and return change
    def processMoney(item):
        global profit
        cost = MENU[item]["cost"]
        q = float(input("How many quarter are you inserting?"))
        d = float(input("How many dime are you inserting?"))
        n = float(input("How many nickel are you inserting?"))
        p = float(input("How many penny are you inserting?"))
        money = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
        if cost > money:
            print("Sorry, that's not enough money. Money refunded")
        else:
            profit += cost
            for res in MENU[item]["ingredients"]:
                resources[res] -= MENU[item]["ingredients"][res]
            if money > cost:
                print(f"Here is ${round((money - cost), 2)} in change.")

    #all prompt options
    prompt = input("What would you like? (espresso/latte/cappuccino):").lower()
    if prompt == "off":
        return
    elif prompt == "report":
        reporting = resources
        reporting["Money"] = f"${profit}"
        return print(reporting)

    if checkResources(prompt):
        processMoney(prompt)

    print(f"Here is your {prompt}. Enjoy!")
    print(resources)
    print(profit)

coffeeMachine()

