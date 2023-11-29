#HOW TO NEST A NEST IN DICTIONARY.
#Nesting Dictionaries in Lists
la_liga = {'teams' : 20, 'ucl' : 19}
epl = {'teams' : 20, 'ucl' : 14}
serie_A = {'teams' : 20, 'ucl' : 10}
ligue_1 = {'teams' : 20, 'ucl' : 1}

leagues = [la_liga, epl, serie_A, ligue_1]
for league in leagues:
    print(league)
print()
#Making an empty list with dictionaries.
futball = []
#assigning players identity
for player in range(11):
    tactic = { 'player' : 'name', 'position' : 'goal keeper', 'number' : 1,}
    futball.append(tactic)
print()
#show first 5
print(futball)
print()
for play in futball[ : 5]:
    print(play)
print('...')
print(f"Total number of players: {len(futball)}.")
print()
#playing with the lists
for players in futball[1 : 4]:
    if players['number'] == 1:
        players['position'] = 'defender'
        print(players)
print(futball[0:5])
print()
#Nest list in dictionary
barca = {
    'league' : 'la liga',
    'titles' : ['la liga', 'copa del rey', 'supercopa', 'ucl'],
    }
mj23 = {
    'mvp' : 5,
    'dpoy' : 1,
    'nba title' : [1991, 1992, 1993, 'hiatus', 1996, 1997, 1998],
    'fmvp' : 6,
    }
print(barca)
print(f"Barcelona, a club in Catalunya, Spain, play in {barca['league'].title()} and is a "
        "successful club that has won:")
for champ in barca['titles']:
    print('\t' + champ)
print()
#Nesting a dictionary in a dictionary
nba = {
        'air jordan' : {
            'mvp' : 5,
            'dpoy' : 1,
            'rings' : 6,
            'ring_yr' : [1991, 1992, 1993, 1996, 1997, 1998],
            'fmvp' : 6,
            'olympic' : ('gold', 2),
        },
        'king james' : {
            'mvp' : 4,
            'dpoy' : 0,
            'rings' : 4,
            'ring_yr' : [2012, 2013, 2016, 2020],
            'fmvp' : 4,
            'olympic' : ['gold-1', 'bronze-1'],
        },
    }
print(nba)
print()
for superstar, allstar in nba.items():
    print(f'Basketball Star: {superstar.title()}')
    star = f"{allstar['mvp']}"
    print(f'He has {star} MVP')
    print()
