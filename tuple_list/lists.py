icons = ['flight23', 'tesla', 'mogulrihanna']
mix = [1, 'sparrow', 'joker', '34']
items = []
magicians = []
cars = []
print(items)
items.extend(['cigar'])
items.extend(['jet'])
print(f'{items}\n')

print(magicians)
magicians += ['houldini']
magicians += ['kyrie']
magicians.append('messi')
magicians.insert(2, 'federer')
print(f'{magicians}\n')

print(mix)
#mix.extend(['ragner'], [10])    syntaxError
mix.extend(['ragner', 10])
print(f'{mix}\n')

print(cars)
cars += ['porsche', 'ferrari', 'mercedes']
print(f'{cars}\n')

'''
print(items); print(magicians); print(mix)
print(cars);
print(icons.index('mogulrihanna'))
'''
items += 'test'
print(items)
print(items.index('t'))
del items[2]
items.pop(3)
icons.extend('star')
print(f'{items}\n')

print(icons)
print(icons.index('s'))
icons.remove('s')
icons.pop()
print(f'{icons}\n')

iconscpy = icons[:]
print(iconscpy)
iconscpy.sort()
print(iconscpy)
iconscpy.reverse()
print(iconscpy)
iconscpy.sort(reverse=True)
print(f'{iconscpy}\n')

items += ['Chopper', 'Boats', 'b']
print(items)
print(sorted(items))
print(sorted(items, key=str.lower))
print(sorted(items, reverse=True))
print(f'{items}')
print()
itemscpy = items[ : ]
print(itemscpy)
items.sort()
print(itemscpy)
