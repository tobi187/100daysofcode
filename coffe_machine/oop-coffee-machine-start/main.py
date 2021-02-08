from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import Money

coffee = CoffeeMaker()
items = Menu()
money = Money()

stop_machine = False

while not stop_machine:
    choice = input(f"What you like? We offer {items.get_items()}: ")

    if choice == "off":
        break
    elif choice == "report":
        coffee.report()
        money.report()
        continue

    item = items.find_drink(choice)

    if not coffee.is_resource_sufficient(item):
        continue

    is_money_enough = money.make_payment(item.cost)
    if is_money_enough:
        coffee.make_coffee(item)




