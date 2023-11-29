#Learning return value and more...
def person_name(first, last, middle=''):
    """Making arguments an option."""
    if middle:
        fullName = f"{first} {middle} {last}"

    else:
        fullName = f"{first} {last}"
        print(f"Welcome, {fullName.title()}.")
    
    return fullName.title()

name = person_name('john', 'abah', 'iklpogidi')
print(name)

name = person_name(first='nelson', last='ogbede')
print(name)
