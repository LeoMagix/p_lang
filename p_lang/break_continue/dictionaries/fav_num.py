#Famous numbers
famous = {
    'jordan' : 23,
    'giannis' : 34,
    'messi' : 10,
    'ronaldo' : 9,
    'ray lewis' : 52,
    }
for nom, no in famous.items():
    #print(f"{nom.title()}: {no}")
    print(f'The G.O.A.T {nom.title()}')
    print(f'\t {no}')
    if nom == 'ronaldo':
        print(f'The real {nom.title()}, R9')
    print()    

no2 = ['lebron', 'c.ronaldo', 'vettel', 'ronaldo']
for great in no2:
    if great not in famous:
        print(f'{great.title()}, you too de try.')
        print()
    else:
        print(f'{great.title()}, I see you.')
