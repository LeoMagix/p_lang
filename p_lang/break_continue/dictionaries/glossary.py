#Imitating dictionaries
gloss = {
        'string' : 'sequence or series of characters',
        'list' : 'items or elements in square brackets',
        'append' : 'method used to add items to a list',
        'len' : 'global function, determines the length of a string, lists, etc',
        }
#print(gloss)
for word, desc in gloss.items():
    print(f'{word.title()}:')
    print(f'\t{desc}.')
    #print('\n')
    print()
