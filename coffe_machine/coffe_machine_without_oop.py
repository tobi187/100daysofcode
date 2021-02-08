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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def sum_money(penny, nickel, dime, quarter):
    nickels = nickel * 5
    dimes = dime * 10
    quarters = quarter * 25
    value = penny + nickels + dimes + quarters
    return float(value / 100)


# choice = input("espresso, latte or cappuccino, e, l or c: ")
#
# penny = int(input("penny: "))
# nickel = int(input("nickel: "))
# dime = int(input("quarter's: "))
# quarter = int(input("quarter: "))

i = True

while i:
    choice = input("espresso, latte or cappuccino, e, l or c: ")

    penny = int(input("penny: "))
    nickel = int(input("nickel: "))
    dime = int(input("quarter's: "))
    quarter = int(input("quarter: "))
    if choice == "e":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"] or \
                resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("you ain't got enough resources")
            continue
        elif sum_money(penny, nickel, dime, quarter) < float(MENU["espresso"]["cost"]):
            print("get more money broke fuck")
            continue
        else:
            payback = sum_money(penny, nickel, dime, quarter) - float(MENU["espresso"]["cost"])
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["water"]
            print(f"here's your espresso and your change of {round(payback, 2)}$. Go fuck yourself")

    if choice == "l":
        if resources["water"] < MENU["latte"]["ingredients"]["water"] or \
                resources["coffee"] < MENU["latte"]["ingredients"]["coffee"] or \
                resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("you ain't got enough resources")
        elif sum_money(penny, nickel, dime, quarter) < float(MENU["latte"]["cost"]):
            print("get more money broke fuck")
        else:
            payback = sum_money(penny, nickel, dime, quarter) - float(MENU["latte"]["cost"])
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            print(f"here's your latte and your change of {round(payback, 2)}$. Go fuck yourself")

    if choice == "c":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"] or \
                resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"] or \
                resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("you ain't got enough resources")
        elif sum_money(penny, nickel, dime, quarter) < float(MENU["cappuccino"]["cost"]):
            print("get more money broke fuck")
        else:
            payback = sum_money(penny, nickel, dime, quarter) - float(MENU["cappuccino"]["cost"])
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            print(f"here's your cappuccino and your change of {round(payback), 2}$. Go fuck yourself")
    else:
        i = False
