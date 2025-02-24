from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
options = menu.get_items()
is_on = True
while is_on:
    order = input(f"What do you want ({options}) ")
    if order == 'report':
        coffee_maker.report()
    elif order == 'off':
        is_on = False
    else:
        drink = menu.find_drink(order)
        if drink == 'None':
            print('')
        else:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                print(f"Thanks for purchasing {drink.name} for {drink.cost} it has {drink.ingredients}")