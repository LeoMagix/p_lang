user = input("Enter user name:\n")
file = 'guests.txt'

with open(file, 'w') as guest:
    guest.write(user)
