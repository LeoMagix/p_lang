#Working With Arbitrary Number of Arguments
#> *args

def pizza(*toppings):
    """Print a list of requested toppings."""
    print(toppings)
pizza('pepperoni')
pizza('extra cheese', 'green peppers', 'mushrooms')

def  make_pizza(*args):         #*args is the generic name to use for a parameter that collects arbitrary arguments.
    """Summarize the kind of pizza we about to make.""" #However for a more easy to understand code use a descriptive name e.g. *toppings
    
    print("\nMaking a pizza with the listed toppings.")
    
    for topping in args:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('extra cheese', 'green peppers')
make_pizza('spinach', 'pepperoni', 'green pepper', 'extra cheese')

#Mixing positional and arbitrary arguments

def make_pizza(size, *toppings):
    """Making a more robust pizza with requested toppings."""
    if size:
        print(f"\nMaking {size}-inch pizza with listed toppings.")
        
        for topping in toppings:
            print(f"- {topping}")                           #can't make it do what i want, which is consider a situation where the user doesn't
                                                            #enter a size.i.e. consider multiple scenerio.
    else:
        print(f"\nMaking a pizza with the list of provided toppings.")
        
        for topping in toppings:
            print(f"> {topping}")

make_pizza(12, 'pepperoni')
"make_pizza('extra cheese', 'green peppers')"
make_pizza(20, 'spinach', 'pepperoni', 'green pepper', 'extra cheese')

