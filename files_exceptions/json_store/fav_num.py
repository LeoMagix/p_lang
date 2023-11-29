import json

def get_stored_num():
    """Get the stored number if available."""
    fave = 'fav_numba.json'
    try:
        with open(fave) as fn:
            numba = json.load(fn)
    
    except FileNotFoundError:
        return None
    
    else:
        return numba

def get_fav_num():
    """Ask user to enter favorite number."""
    fav_numba = input("What's your favorite number?\n")
    fave = 'fav_numba.json'
    
    with open(fave, 'w') as fn:
        json.dump(fav_numba, fn)
    return fav_numba

def check_num():
    """Confirm if favorite number is correct."""
    current_fav = get_stored_num()
    print("Enter 'y' to confirm favorite number.")
    ask = input(f"Is this your favorite number?-{current_fav}.\n")

    if ask == 'y':
        print(f"I know your favorite number! It's {current_fav}.")
    else:
        new_fav = get_fav_num()
        print(f"I have stored {new_fav} as your favorite number.")

def show_fav_num():
    """Display the users favorite number."""
    numba = check_num()

#print(get_stored_num())
#print(get_fav_num())
show_fav_num()
