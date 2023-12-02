#EVERYTHING YOU CAN DO WITH RETURN IN A FUNCTION:
#1.making optional arguments optimal-:
def get_fullName(first, last, middle=''):
    """Using return to output formatted full name."""
    if middle:
        fullName = f"{first} '{middle}' {last}"
    
    else:
        fullName = f'{first} {last}'
    
    return fullName.title()

nom = get_fullName('2pac', 'shakur')

person_name = get_fullName('kendrick', 'lamar', 'kungfu kenny')

print(f"THUG life- {nom}.")

print(f'Call me {person_name}.')

print()

def bio_info(name, study, age=None):
    """Just a simple bio data information."""
    print("provide name, study, age:")
    
    if age:
        bio = f"{name}; {study}; {age}."
    
    else:
        bio = f"{name}; {study}."
    
    return bio

data = bio_info('billy', 'mai ruwa', 19)
print(data)

print()

bio = bio_info('smarty', 'fishing') #"you fit use same variable label  inside a funtion outside a function to store different values.
print(bio)

print()

#2.Return value and dictionary-:
def build_person(name, age):
    """Returning a dictionary of information."""
    person = {'name' : name, 'age' : age}
    
    return person, 'stroke'

person = build_person('akpa', 12)
print(person)
