nba = {
        'air jordan' : {
            'mvp' : 5,
            'dpoy' : 1,
            'rings' : 6,
            'ring year' : [1991, 1992, 1993, 1996, 1997, 1998],
            'fmvp' : 6,
            'olympic' : ('gold', 2),
        },
        'king james' : {
            'mvp' : 4,
            'dpoy' : 0,
            'rings' : 4,
            'ring year' : [2012, 2013, 2016, 2020],
            'fmvp' : 4,
            'olympic' : ['gold-1', 'bronze-1'],
        },
    }
nba['king james']['olympic'][0] = 'gold-2'
print("Michael Jordan vs LeBron James.\n")
for star, wins in nba.items():
    print(f'{star.upper()}')
    for award, num in wins.items():
        if award == 'ring year':
            print('Number of NBA Titles.')
            print(f'{award.title()}:')
            for no in num:
                print(no)
            print()
        elif award == 'olympic':
            print(f'{award.title()} medal:')
            for no in num:
                print(no)
            print()
        
        elif award != 'ring year' or award != 'olympic':
            print(f'{award.title()}:')
            print(num)
            print()
    print()
