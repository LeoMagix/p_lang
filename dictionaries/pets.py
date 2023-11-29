#Who keeps a pet?
pet_dog = {'pet' : 'dog', 'name' : 'obagu', 'owner' : 'johnbull',}
pet_cat = {'pet' : 'cat', 'name' : 'mumuni', 'owner' : 'stella',}
pet_lion = {'pet' : 'lion', 'name' : 'growl', 'owner' : 'el khaled',}
pets = []
pets.extend([pet_dog, pet_cat, pet_lion])
#print(pet)
for pet in pets:
    for i, v in pet.items():
        print(f"{i.upper()}- {v.title()}")
    print()
