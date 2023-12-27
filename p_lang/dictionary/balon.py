"""Simple program to store  a list in a dictionary."""

#Create a dictionary of football players as keys and 
#list of years they've won the balon d'or as values.
#Then store this keys:values pair in a collective dictionary.

world_best = {
        'de lima ronaldo' : {
            'country':['brasil'],
            'Balon d\'or':[1997, 2002],
            'fifa best':[],
            'fifa world cup':[1994,2002],
            'fifa golden ball':[],
            },
        'ronaldinho' : {
            'country':['brasil'],
            'balon d\'or':[2005],
            'fifa best player':[2005,2006],
            'fifa world cup':[2002],
            'fifa golden ball':[2002],
            },
         'cristiano ronaldo': {
             'country':['portugal'],
             'balon d\'or':[2008,2013,2014,2016,2017],
             'fifa best player':[2016, 2017],
             'fifa world cup':['nil'],
             'fifa golden ball':['nil'],
             },
         'lionel messi': {
             'country':['argentina'],
             'balon d\'or':[2009,2010,2011,2012,2015,2019,2021,2023],
             'fifa  best player':[2021,2022],
             'fifa world cup':[2022],
             'fifa golden ball':[2014,2022],
             },
         'luka modric': {
             'country':['croatia'],
             'balon d\'or':[2018],
             'fifa best':[2018],
             'fifa world cup':['nil'],
             'fifa golden ball':[2018],
             },

          'karim  benzema': {
            'country':['france'],
            "balon d'or":[2022],
            'fifa best':[],
            'fifa world cup':['nil'],
            'fifa golden ball':['nil'],
            'club':['real madrid'],
            },
         'zinedine zidane': {
             'country':['france'],
             'balon d\'or':[1998],
             'fifa best':[],
             'fifa world cup':['1998'],
             'fifa golden ball':[1998],
             'club':['juventus'],
             },
         }

world_best['de lima ronaldo']['club']=['inter milan', 'real madrid']
world_best['ronaldinho']['club']=['barcelona']
world_best['cristiano ronaldo']['club']=['manchester united', 'real madrid']
world_best['lionel messi']['club']=['barcelona', 'paris saint german']
world_best['luka modric']['club']=['real madrid']

for player, awards in world_best.items():
    print(f'{player.upper()}-')
    for award_name, award_year in awards.items():
        print(f"{award_name.title()}:")
        for aw_yr in award_year:
            print(f'\t*{str(aw_yr).title()}')
    print()

la_pulga = world_best['lionel messi']["balon d'or"]
num = len(la_pulga)
record = f"Lionel Messi has a record setting {num} balon d'ors."
print(record)

cr7 = world_best['cristiano ronaldo']["balon d'or"]
num2 = len(cr7)
numtwo = f"The closest is Cristiano Ronaldo with {num2} balon d'or awards."
print(numtwo)
