#Dinner reservations for legends
guests = ['michael jordan', 'nikola tesla', 'elon musk']
print(f'{guests[0].title()}, I would like to invite you to dinner at Precepts Resorts.')
print(f'{guests[1].title()}, I would like to invite you to dinner at Precepts Resorts.')
print(f'{guests[2].title()}, I would like to invite you to dinner at Precepts Resorts.\n')

print(f'{guests[-1].title()} is unavailable.\n')

guests[-1] = 'zara hadid'
print(f'{guests[2].title()}, I would like to invite you to dinner at Precepts Resorts.')
print(f'{guests[0].title()}, I would like to invite you to dinner at Precepts Resorts.')
print(f'{guests[-2].title()}, I would like to invite you to dinner at Precepts Resorts.\n')

guests.insert(-1, 'usain bolt')
guests.insert(2, 'shelly ann fraser')
guests.extend(['giannis'])
print('There is room for extended dinner reservations.\n')
print(f'{guests[2].title()}, I would like to invite you to dinner at Precepts Resorts.')
print(f'{guests[-1].title()}, I would like to invite you to dinner at Precepts Resorts.')
print(f'{guests[-2].title()}, I would like to invite you to dinner at Precepts Resorts.\n')

print('You can only accomodate two persons at the table.\n')
#print(len(guests))

disappoint1 = guests.pop(-1)
disappoint2 = guests.pop(-2)
disappoint3 = guests.pop()
disappoint4 = guests.pop()
print(f"Sorry {disappoint1.title()}, we can't host at dinner anymore.")
print(f"Sorry {disappoint2.title()}, we can't host you at dinner anymore.")
print(f"Sorry {disappoint3.title()}, we can't host you at dinner anymore.")
print(f"Sorry {disappoint4.title()}, we can't host you at dinner anymore.\n")

print('Persons still on the reservations')
print(f'{guests[0].title()}, you are still on for dinner')
print(f'{guests[1].title()}, you are still on for dinner')

del guests[0]
del guests[0]
print(guests)
