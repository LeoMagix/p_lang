#voyage de dictionarie
tour = {'paris' : 'eiffel', 'egypt' : 'pyramid', 'dubai' : 'burj khalifa'}
print(tour)
print(type(tour))
print(tour['paris'])
print(tour['egypt'].title())
tallest_building = tour['dubai']
print(f"One of the greatest feat of engineering, {tallest_building.title()}.")
#expanding ur dictionary
tour['rome'] = 'basilica'
print(tour)
#working with empty dictionaries
f1_drivers = {}
f1_drivers['mercedes'] = 'hamilton'
f1_drivers['aston martrin'] = 'alonso'
f1_drivers['ferrari'] = 'vettel'
print(f1_drivers)
#modifying ur dictionary
alien0 = {'color':'violet', 'points':5, 'level':1}
print(alien0)
alien0['level'] = 3
alien0['points'] = 10
alien0['color'] = 'red'
print(alien0)
#deleting key-value pairs
del alien0['level']
print(alien0)
#copy copy
alien00 = alien0.copy()
alien00['level'] = 2
print(f'\n{alien0}')
print(alien00)
#other ways to clean ur dictionary less permanenly
oshe = alien00.pop('level')
print(alien00)
print(oshe)
alien00.popitem()
print(alien00)

print(f'\n{len(alien0)}')
print(len(alien00))

gwen = list(alien0)
print(gwen)
print(list(alien0.keys()))
print(list(alien0.values()))

balonDor = {
    'kaka' : 'ac milan',
    'c.ronaldo' : 'man utd',
    'messi' : 'barcelona',
    'modric' : 'real madrid',
    }
print(balonDor)

cars = {
    'italy' : 'ferrari',
    'germany' : 'mercedes',
    'japan' : 'toyota',
    'england' : 'aston martin',
    }
uk = cars['england']
print(f"\n{uk.title()} is the pride of London.")
get = cars.get('japan')
print(get)
brits = cars.get('england', 'rolls royce')
print(brits)
print(cars.get('india', 'There is no indian car here.'))

#for loop in dictionary
for city, car in cars.items():
    print(f'\nCity: {city}')
    print(f'Car: {car}')

for city in cars.keys():
    print(f'\n{city.upper()}')
print()

for baller in balonDor:
    print(baller.title())
print()

for baller in sorted(balonDor.keys()):
    print(f'{baller}')
print()

for club in balonDor.values():
    print(club.title())
print()

for club in sorted(balonDor.values()):
    print(club.title())
print()

test = {2002 : 'zidane'}        #this is legit.
print(test)
print(test.keys())
print(balonDor.keys())
print()

popular_lang = {
        2000 : 'c',
        2002 : 'c',
        2005 : 'java',
        2010 : 'python',
        2020 : 'python',
        }
print(popular_lang)
for lang in set(popular_lang.values()):
    print(lang.upper())
