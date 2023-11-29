import json
#REFACTORED PROGRAM
#Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
def get_stored_username():
    """Get stored username if available."""
    user = 'usr_name.json'     
    try:
        with open(user) as fo:
           usr = json.load(fo)

    except FileNotFoundError:
        return  None

    else:
        return usr

def get_new_username():
    """Prompt for a new username."""
    usr_name = input("What's your username?\n")
    user = 'usr_name.json'
    with open(user, 'w') as f:
        json.dump(usr_name, f)
    return usr_name

def verify_username():
    """Checks if username is a new entry."""
    prev_user = get_stored_username()
    verify = input(f"Is this your username? {prev_user}:y/n\n")
    
    if verify == 'y':
        print(f"Welcome back, {prev_user}!")
    
    elif verify == 'n':
        current_usr = get_new_username()
        print(f"We'll remember you {current_usr}, when you come back.")
 
    else:
        print("Please enter a valid response.")

def greet_user():
    """Greet user by name."""
    user = verify_username()
'''
    user = get_stored_username()
   
    if user:
        print(f"Welcome back, {user}!")
    
    else:
        usr = get_new_username()
        print(f"We'll remember you {usr_name}, when you come back.")
'''

#print(get_stored_username())
#print(get_new_username())
#verify_user()
greet_user()
