from art import coffees, latte, espresso, cappuccino
from coffe_data import MENU
print(coffees)
print(espresso)
print(latte)
print(cappuccino)

water=900
milk=900
coffee=500
cost=0


def enjoy_your_cofee(choice):
    print(f"Here is your {choice} 🍵 enjoy!")


def report(water_needed,milk_needed,coffee_needed,cost_coming):
    print(f"Water:{water_needed}")
    print(f"Milk:{milk_needed}")
    print(f"Coffee:{coffee_needed}")
    print(f"Money:${cost_coming}")


def espresso(MENU):
    global water
    global coffee
    global cost
    water = water - MENU["espresso"]["ingredients"]["water"]
    milk = 0
    coffee = coffee - MENU["espresso"]["ingredients"]["coffee"]
    cost = cost + MENU["espresso"]["cost"]


def latte(MENU):
    global water
    global coffee
    global cost
    global milk
    water = water - MENU["latte"]["ingredients"]["water"]
    milk = milk - MENU["latte"]["ingredients"]["milk"]
    coffee = coffee - MENU["latte"]["ingredients"]["coffee"]
    cost = cost + MENU["latte"]["cost"]

def check_availability(choice):
    global water
    global milk
    global coffee
    count=0
    water_resource=MENU[choice]["ingredients"]["water"]
    if choice=="espresso":
        milk_resource = 0
    else:
        milk_resource=MENU[choice]["ingredients"]["milk"]
    coffee_resource=MENU[choice]["ingredients"]["coffee"]
    if water_resource>water:
        print("Sorry there is not enough water in the machine left")
        count+=1
    elif milk_resource>milk:
        print("Sorry there is not enough milk in the machine left")
        count+=1
    elif coffee_resource>coffee:
        print("Sorry there is not enough coffee in the machine left")
        count+=1

    return count
def cappuccino(MENU):
    global water
    global coffee
    global milk
    global cost
    water = water - MENU["cappuccino"]["ingredients"]["water"]
    milk = milk - MENU["cappuccino"]["ingredients"]["milk"]
    coffee = coffee - MENU["cappuccino"]["ingredients"]["coffee"]
    cost = cost + MENU["cappuccino"]["cost"]


def taking_coins(value_of_coffee,choice):
    penny = float(input("How many pennies?:"))
    dime = float(input("How many dimes?:"))
    nickel = float(input("How many nickels?:"))
    quarter = float(input("How many quarters?:"))
    penny=penny*0.01
    dime=dime*0.10
    nickel=nickel*0.05
    quarter=quarter*0.25
    continue_coffee = True
    total_coins_value = penny + dime + nickel + quarter
    total_left_money = total_coins_value - value_of_coffee
    if total_left_money > 0:
        continue_coffee = True
        print(f"Here is ${total_left_money} in change 😇")
        enjoy_your_cofee(choice)
    else:
        continue_coffee = False
        print("You don't have enough money sorry! 🥲")
    return continue_coffee


coffe_machine=True

while coffe_machine==True:
    choice = input("What Would You Like ?:").lower()
    if choice == "espresso":
        if check_availability(choice)==0:
            taking_coins(MENU["espresso"]["cost"], choice)
            espresso(MENU)

    elif choice == "latte":
        if check_availability(choice)==0:
            taking_coins(MENU["latte"]["cost"], choice)
            latte(MENU)

    elif choice == "cappuccino":
        if check_availability(choice)==0:
            taking_coins(MENU["cappuccino"]["cost"], choice)
            cappuccino(MENU)

    elif choice == "report":
        report(water, milk, coffee, cost)

    elif choice == "off":
        coffe_machine = False