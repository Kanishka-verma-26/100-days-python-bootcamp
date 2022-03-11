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
        "cost": 3.8,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_ing_sufficient(ing):
    print("Water :", ing['water'])
    print("Milk :", ing['milk'])
    print("Coffee :", ing['coffee'])
    if resources['water'] <= ing['water'] or resources['milk'] <= ing['milk'] or resources['coffee'] <= ing['coffee']:
        return False
    else:
        return True


def process_coins():
    print("Please insert coins!")
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.1
    total += int(input("How many nickels? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        print("Please try again to get your coffee. ")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True


def make_coffee(ch, ing):
    for i in ing:
        resources[i] -= ing[i]
    print(f"Here is your {ch}. ")


def main():
    # ch='latte'
    ch = input("What would you like to have? (espresso/latte/cappuccino) : ").lower()
    if ch == "off":
        print("Thankyou for using")
        return
    elif ch == 'report':
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"profit : ${profit}")
    else:
        drink = MENU[ch]
        ing = drink['ingredients']
        if is_ing_sufficient(ing):
            money_received = process_coins()
            if is_transaction_successful(money_received, drink['cost']):
                make_coffee(ch, ing)

        else:
            print("Sorry, there are not enough ingredients for your drink!!")

    main()


main()