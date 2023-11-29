#Requesting Requested Requests of Pizza Toppings.
pizza = 'Enter requested pizza toppings.\n'
pizza += ("Enter 'quit' to exit finish requests:\n")
lst = ['pepperoni', 'crust', 'salad']

topping = " "
while topping != 'quit':
    topping = input(pizza)
    print()
    if topping != 'quit':
        if topping not in lst:
            break
        else:
            print(topping)
            print()
    else:
        print("See you later.")
