from menu import Menu, MenuItem
from coffee_maker import Coffeemaker
from money_machine import money

coffee = Coffeemaker()
items = Menu()
money = money()

stop_machine = False

while not stop_machine:
    choice = input(f"What you like? We offer")
    if choice == "off":
        break
    elif choice == "report":
        coffee.report()
        money.report()
    elif not items.find_drink(choice):
        print(f"enter valid drink idiot not fucking {choice}")
        continue
    elif not coffee.is_resource_sufficient(choice):
        coffee.is_resource_sufficient(choice)
        continue

    pennys = int(input("pennys: "))
    dimes = int(input("dimes: "))
    nickles = int(input("nickels: "))
    quarters = int(input("quarters: "))

    value = pennys * 0.01 + dimes * 0.05 + nickles * 0.10 + quarters * 0.25

    money.make_payment(value)

    if money.make_payment(value):
        coffee.make_coffee(choice)



