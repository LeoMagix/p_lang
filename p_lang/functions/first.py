#Writing My First Python Function.
def first():
    """Bon voyage a` funtion."""
    print("My first Python function program ever.")

first()

def user_info(name, age, location='earth'):
    """A little description about our user."""
    print("Tell us a little about yourself\n")
    name = input("What's your name?\n")
    print()
    age = int(input('And your age please?\n'))
    print()
    location = input("Where do you stay?\n")
    print()
    
    if location == '':
        location = 'earth'

    print(f"The {name}; {age}: {location}.")

user_info('name', 'age', 'location')
