#Smoking on top 5's-NBA players
nba = {
        'micheal jordan' : {
            'nickname' : 'air jordan',
            'mvp' : 5,
            'dpoy' : 1,
            'rings' : 6,
            'fmvp' : 6,
            },
        'lebron james' : {
            'nickname' : 'king james',
            'mvp' : 4,
            'dpoy' : 0,
            'rings' : 4,
            'fmvp' : 4,
            },
        'kobe bryant' : {
            'nickname' : 'black mamba',
            'mvp' : 1,
            'dpoy' : 0,
            'rings' : 5,
            'fmvp' : 2,
            },
        }
nba['micheal jordan'][ 'seasons'] = 14
nba['lebron james']['seasons'] = 21
nba['kobe bryant']['seasons'] = 20
#print(nba)
for star, bio in nba.items():
    print(f"{star.upper()}:")
    for wins, info in bio.items():
        print(f'\t{wins.title()} - {info}')
    print()
