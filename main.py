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
    "water": 1300,
    "milk": 1200,
    "coffee": 1100
}

coffee_machine_on = True
profit = 0

while coffee_machine_on:
    coffee_options = input('What would you like? (espresso/latte/cappuccino): ').lower()
    
    def calculate_coins():
        """ calculates profits, produces coffee, and refunds money """
        global profit
        coffee = MENU[coffee_options]
        print('Please insert coins.')
        quarters = int(input('how many quarters?: '))
        dimes = int(input('how many dimes?: '))
        nickles = int(input('how many nickles?: '))
        pennies = int(input('how many pennies?: '))
        
        profit += coffee['cost']
        total = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
        refund = total - coffee['cost']
        format_refund = '${:.2f}'.format(refund)

        if refund >= 0:
            print(f'\nHere is {format_refund} in change.')
            print(f'Here is your {coffee_options} ☕️. Enjoy!\n')
            return profit
        else:
            print("Sorry that's not enough money. Money refunded.\n")


    def update_resources():
        """ tracks and updates coffee ingredients """
        coffee = MENU[coffee_options]
        ingredients = coffee['ingredients']
        for key, value in ingredients.items():
            # print(key, resources[key], value)
            resources[key] = resources[key] - value
            if resources[key] <= 0:
                print(f'Sorry there is not enough {key}.')
                refill_resources = input(f'Do you want to refill the {key}? y/n: ').lower()
                if refill_resources == 'y':
                    resources[key] = 1000 - value
                else:
                    print('Coffee machine out of service...\n')
                    exit()
        return resources


    def report():
        """ Prints report of ingredients and profit """
        for key, value in resources.items():
            print(f'{key}: {value}')
        print('Money: ${:.2f}\n'.format(profit))


    if coffee_options in MENU:  # create coffee
        update_resources()
        calculate_coins()
    elif coffee_options == 'report':  # print report
        report()
    elif coffee_options == 'off':  # end loop
        coffee_machine_on = False
