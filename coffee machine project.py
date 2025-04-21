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


def add(n1):
    count_down = int(n1)
    total = 0
    num = 0.25
    while count_down > 0:
        total += num
        num += 0.25
        count_down -= 1
        if count_down == 0:
            return total


def add1(n2):
    count_down = int(n2)
    total1 = 0
    num = 0.10
    while count_down > 0:
        total1 += num
        num += 0.10
        count_down -= 1
        if count_down == 0:
            return total1


def add2(n3):
    count_down = int(n3)
    total2 = 0
    num = 0.05
    while count_down > 0:
        total2 += num
        num += 0.05
        count_down -= 1
        if count_down == 0:
            return total2


def add3(n4):
    count_down = int(n4)
    total3 = 0
    num = 0.01
    while count_down > 0:
        total3 += num
        num += 0.01
        count_down -= 1
        if count_down == 0:
            return total3


def add4(m1, m2, m3, m4):
    return m1 + m2 + m3 + m4


def products(pm):
    for item in MENU[pm]["ingredients"]:
        resources[item] -= MENU[pm]["ingredients"][item]
    print("\nupdated Resources:")
    for key, value in resources.items():
        print(f"{key.capitalize()}:{value}ml")
        print("-"*20)


def costs(mp, m4):
    return mp - m4


def cal(col):
    if col == "espresso":
        if resources["water"] >= MENU[col]["ingredients"]["water"] and resources["coffee"] >= \
                    MENU[col]["ingredients"]["coffee"]:
            print(f"You can make an {col}")
            return sun > 0
        else:
            print(f"Not enough resources an {col}")
            return sun < 0
    elif col in ["latte", "cappuccino"]:
        if resources["water"] >= MENU[col]["ingredients"]["water"] and resources["coffee"] >= \
                    MENU[col]["ingredients"]["coffee"] and resources["milk"] >= MENU[col]["ingredients"]["milk"]:
            print(f"The are enough resources for a {col}")
            return sun > 0
        else:
            print(f"Not enough resources for a {col}")
            return sun < 0



sun = 1
profit = 0
while sun > 0:
    kamo = input("What would you like?(espresso/latte/cappuccino):").lower()
    if kamo == "off":
        break
    elif kamo in MENU:
        if cal(kamo):
            print("Please insert coin")
            coin1 = int(input("How many quarters : "))
            coin2 = int(input("How many dimes : "))
            coin3 = int(input("How many nickles : "))
            coin4 = int(input("How many pennies : "))

            omo = add4(add(coin1), add1(coin2), add1(coin3), add3(coin4))
            rounded_num = round(omo,2)
            if omo == MENU[kamo]["cost"]:
                print(f"The amount payed is sufficient for an {kamo} ")
                print("The amount of resources left are:")
                products(kamo)
                print("Theres no change")
                print(f"Here is your {kamo}.Enjoy!")
            

            elif omo > MENU[kamo]["cost"]:
                print(f"The amount payed is:{rounded_num}")
                print("The amount of resources left are:")
                products(kamo)
                result = costs(omo, MENU[kamo]["cost"])
                result_num = round(result, 2)
                print(f"Your change is:{result_num}")
                print(f"Here is your {kamo}.Enjoy!")

            elif omo < MENU[kamo]["cost"]:
                print("The amount payed is insufficient")
                break

            else:
                print("error")
            profit += MENU["cappuccino"]["cost"]
            print(f"profit gained:R{profit}")
        else:
            print("\nMachine is out of resources!Turning off..... ")
            break
    elif kamo == "report":
        print(f"water:{resources['water']}")
        print(f"milk:{resources['milk']}")
        print(f"coffee:{resources['coffee']}")
        ntshala = input("What would you like?(espresso/latte/cappuccino):").lower()
        if Ntshala == "off":
            break
        elif cal(Ntshala):
            print("Please insert coin")
            coin1 = int(input("How many quarters : "))
            coin2 = int(input("How many dimes : "))
            coin3 = int(input("How many nickles : "))
            coin4 = int(input("How many pennies : "))

            omo = add4(add(coin1), add1(coin2), add1(coin3), add3(coin4))
            rounded_num = round(omo, 2)
            if omo == MENU[Ntshala]["cost"]:
                print(f"The amount payed is sufficient for an {Ntshala} ")
                print("The amount of resources left are:")
                products(Ntshala)
                print("Theres no change")
                print(f"Here is your {Ntshala}.Enjoy!")


            elif omo > MENU[Ntshala]["cost"]:
                print(f"The amount payed is: {rounded_num}")
                print("The amount of resources left are:")
                products(Ntshala)
                result = costs(omo, MENU[Ntshala]["cost"])
                result_num = round(result, 2)
                print(f"Your change is:{result_num}")
                print(f"Here is your {Ntshala}.Enjoy!")


            elif omo < MENU[Ntshala]["cost"]:
                print("The amount payed is insufficient")
                break

            else:
                print("error")
                break
        else:
            print("\nMachine is out of resources!Turning off..... ")
            break
    else:
        print("error")

