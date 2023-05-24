from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffeeMachine():
    cm = CoffeeMaker()
    m = Menu()
    mm = MoneyMachine()
    on = True

    while on:
        prompt = input(f"What would you like {m.get_items()}").lower()
        if prompt == "report":
            cm.report()
            mm.report()
        elif prompt == "off":
            on = False
        else:
            drink = m.find_drink(prompt)
            if cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
                cm.make_coffee(drink)
                mm.report()
                cm.report()

coffeeMachine()