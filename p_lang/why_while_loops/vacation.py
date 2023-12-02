#Poll for Vacationing.
destination = {}

dream = True
while dream:
    name = input("What's your name?\n")
    print()
    response = input("Where would be your dream vacation?: ")
    print()
    destination[name] = response
    poll = input("Would anybody else like to respond? (yes/no)-- ")
    print()
    if poll == 'no':
        dream =  False
        print("Okay.\n")
for name, vacation in destination.items():
    print(f"{name.title()} would like to visit {vacation.title()}!")
