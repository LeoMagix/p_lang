#People wey like to waka and where dem de like go.
favorite_places = {
        'freshest' : ['ribadu', 'queen amina', 'social center'],
        'collins' : ['social center', 'chillax spot', 'party'],
        'isayi' : ['jo benson', 'quilox', 'club'],
        }

yawo = f"These guys no de stay for house, see their favorite joints."
print(f'{yawo.upper()}')
print('\n')
for waka, place in favorite_places.items():
    print(f"{waka.upper()}-")
    for area in place:
        print(f'\t{area.title()}.')
    print()
