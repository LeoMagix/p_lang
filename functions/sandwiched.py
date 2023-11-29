#Defining a function with a parameter that accepts an arbitrary number of arguments.
def make_sandwich(*sandwich):
    """Making a sandwich with a list of provided items."""
    
    print("\nMaking your sandwich with provided ingredients:")
    
    for item in sandwich:
        print(f'>{item}')

    print("Your sandwich is ready.")

make_sandwich('lettuce')

make_sandwich('onions', 'carbage')
