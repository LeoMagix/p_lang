#The rich and famous
forbes = {
        'Billonaires' : ['musk', 'bezos', 'dangote'],
        'millonaires' : ['kanye', 'shaq', 'elemelu'],
        }
for worth, person in forbes.items():
    print(worth + ':')
    #print(person)
    for rich in person:
        print('\t' + rich)
        print()
