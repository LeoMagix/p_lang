'''
players = []
players[0:4] = 'ronaldo delima', 'messi', 'ronaldinho'
print(players)

players += ['c.ronaldo', 'neymar', 'xavi', 'robben']
list_lenght = len(players)
print(f"Our list constains {list_lenght} players.")

print(f"\nList of players that have won the prestigious Balon d'or award:")
for player in players[0:4]:
    print(f"-\t{player.title()}")
    if player == 'messi':
        print(f"\tLionel Messi has 8 balon d'ors.\n")
    
    elif player == 'ronaldo delima':
        print(f"\tRonaldo delima Nazario has 3 balon d'ors.\n")
    
    elif player == 'ronaldinho':
        print(f"\tRonaldinho Gaucho has 1 balon d'or.\n")

    else:
        print(f"\tCristiano Ronaldo has 5 balon d'ors.\n")
'''
q = 0
while True:
    sports = [['messi', 'ronaldinho', 'ronaldo'], ['jordan', 'olajuwon', 'giannis'], ['djokovic', 'federer', 'nadal']]
    for top3s in sports:
        q += 1
        for top3 in top3s:
            print(top3, end=' ')
        print(f'{q}')
    break;
