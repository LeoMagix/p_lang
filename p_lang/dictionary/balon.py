"""Simple program to store  a ilst in a dictionary."""

#Create a  dictionary of football palyers as keys and a'
#list of years they won the balon d'or as values.
#Then store this keys:values pair in a common dictionary.

world_best = {
        'ronaldo de lima nasario' : {
            'country':['brasil'],
            'Balon d\'or':[1999, 2002],
            'fifa best':[],
            'fifa world cup':[1994,2002],
            'fifa g=olden ball':[],
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
             'balon d\'or':[2009,2010,2011,2012,2015,2019,2021,2022],
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
         }

for player, awards in world_best.items():
    print(f'{player.upper()}-')
    for award_name, award_year in awards.items():
        print(f"{award_name.title()}:")
        for aw_yr in award_year:
            print(f'\t*{aw_yr}')
    print()
