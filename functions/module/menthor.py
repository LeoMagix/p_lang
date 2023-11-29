#More functions and module.
def name_user(first, last):
    """Print the name of a specific user."""
    users_name = f'{first.title()} {last.title()}'
    client = f"\nThe client is {users_name}"

    return client

def call_user(first, last):
    """Calls the attention of the user."""
    users_name = f'{first.title()} {last.title()}'
    print(f"\n{users_name.upper()}, the boss will see you now.")
