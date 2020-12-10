MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def make_coffee():
    coffee = input('What would you like? (espresso/latte/cappuccino): ')

    if coffee == 'espresso':
        return MENU['espresso']
    elif coffee == 'latte':
        # print(MENU['latte'])
        return MENU['latte']
    elif coffee == 'cappuccino':
        # print(MENU['cappuccino'])
        return MENU['cappuccino']


def calculate_coins(coffee):
    print('Please insert coins.')
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))

    total = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
    refund = total - coffee['cost']
    format_refund = '${:.2f}'.format(refund)

    # print(MENU[coffee])

    if refund >= 0:
        print(f'Here is {format_refund} in change.')
        if coffee['cost'] == 1.5:
            print(f'Here is your espresso ☕️. Enjoy!')
        elif coffee['cost'] == 2.5:
            print(f'Here is your latte ☕️. Enjoy!')
        elif coffee['cost'] == 3.0:
            print(f'Here is your cappuccino ☕️. Enjoy!')
    else:
        print("Sorry that's not enough money. Money refunded.")


def check_resources():
    pass


def report():
    pass


coffee = make_coffee()
calculate_coins(coffee)