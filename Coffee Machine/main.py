from Coffee_Type import MENU
from Coffee_Type import resources

switch = True


def check_resources(ask, resources):
    if (MENU[ask]["ingredients"]["water"] <= resources["water"]) and (MENU[ask]["ingredients"]["milk"] <= resources["milk"]) and (MENU[ask]["ingredients"]["coffee"] <= resources["coffee"]):
        pennies = int(input("number of pennies: "))
        quarter = int(input("number of quarter: "))
        dimes = int(input("number of dimes: "))
        nickles = int(input("number of nickels: "))
        cash_input = pennies*0.01 + quarter*0.25 + dimes*0.1 + nickles*0.05
        if cash_input >= MENU[ask]["cost"]:
            print(f"Enjoy your {ask}")
            print(f"Here's Your change {cash_input - MENU[ask]["cost"]}")
            resources["water"] -= MENU[ask]["ingredients"]["water"]
            resources["milk"] -= MENU[ask]["ingredients"]["milk"]
            resources["coffee"] -= MENU[ask]["ingredients"]["coffee"]
        else:
            print("Sorry not enough money, Money Returned")
    else:
        print(f"Sorry {ask} is not available")


while switch == True:
    ask = input("What do you want(espresso/latte/cappuccino): ")
    if ask == 'espresso' or ask == 'latte' or ask == 'cappuccino':
        check_resources(ask, resources)
    elif ask == 'report':
        print(f"Water = {resources["water"]}\n milk = {resources["milk"]}\n coffee = {resources["coffee"]}")
    elif ask == 'off':
        switch = False
    else:
        print("Sorry we don't have that, please order something else")