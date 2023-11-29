#List of players with a balon d'or
ballers = ['ronaldo', 'ronaldinho', 'messi', 'c.ronaldo', 'zidane']
print(ballers)
print()

ballers += ['modric']
ballers += (['kaka', 'lukaku'])
ballers.extend(['weah', 'rivaldo', 'sterling'])
print(ballers)
print()
ballers.remove('sterling')
print(ballers)
print()

l = ballers.index('lukaku')
print(l)
lakaka = ballers.pop(7)
print(f"{lakaka.title()} has never won a Balon d'OR.")
print()
print(ballers)
print(len(ballers))

ballz = ballers[0:4]
print()
print(ballz)
del ballers[-4:]
print()
print(ballers)
print(len(ballers))

ballers[2:3] += ['rivaldo', 'romario']
print(ballers)
print()

print(sorted(ballers))
print(ballers)
print()

ballers.sort()
print(ballers)
print()

ballers.reverse()
print(ballers)
print()

ballers.append('Weah')
ballers.sort()
print(ballers)
print()

ballers.sort(key=str.lower)
print(ballers)

