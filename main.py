from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


def main():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    go_on = True
    while go_on:
        print(menu.get_items())
        choice = input("please enter the name of a drink: ").lower()
        drink = menu.find_drink(choice)
        if choice == "off":
            return
        elif choice == "report":
            print(coffee_maker.report(), money_machine.report())
        else:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


main()
