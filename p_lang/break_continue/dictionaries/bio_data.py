#Embedding dictionary in lists
bio = []
tesla = {
        'first name' : 'nikola',
        'last name' : 'tesla',
        'country' : 'serbia',
        'occupation' : 'inventor',
        'alias' : 'master of electricity',
        }
zara = {
        'first name' : 'zara',
        'last name' : 'hadid',
        'country' : 'lebanon',
        'occupation' : 'architect',
        'alias' : 'queen of curves',
        }
musk = {
        'first name' : 'elon',
        'last name' : 'musk',
        'country' : 'south africa',
        'occupation' : 'engineer',
        'alias' : 'techking',
        }
bio.append(tesla)
bio.append(zara)
bio.append(musk)
#print(bio)
for info in bio:
    #print(info)
    for data, detail in info.items():
    #for data, detail in sorted(info.items()):
        print(f'{data.upper()}: {detail.title()}')
    print()
