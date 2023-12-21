"""We'll put a dictionary inside another dictionary, how cool!"""

#Create individual dictionary, store details of persons that possess 
#atrributes, values I admire.
#Then put the information in a collective dictionary named 'mentors'

mentors = {
        'jordan': {
            'fulname' : 'michael jeffrey jordan',
            'profession' : 'basketball',
            'country' : 'u.s.a',
            'nickname' : 'air jordan',
            'attributes' : "competiveness, confidence, self-belief",
            'values' : 'work ethic, focus, committment, goal-driven, courage, optimistic',
            'accomplishment' : '6fmvps, 6rings, 5mvps, 2 olympic golds, billionaire',
            },

        'tesla': {
            'fullname' : 'nikola tesla',
            'profession' : 'electric emgineer, inventor',
            'country' : "serbia-croatia",
            'nickname' : 'master of lightening',
            'attributes' : 'creativity, innovativeness, intelligence,vision',
            'values' : 'priorities, dedication, focus, life-long committment to goals',
            'accomplishment' : 'a.c. current, countless futuristic innovations'
            },

        'musk': {
            'fullname' : 'ELon musk',
            'profession' : 'scientist, engineer, business man',
            'country' : 'south africa, u.s.a',
            'nicjname' : 'techking',
            'attributes' : 'learning, vision, resourcefulness, knowledge, innovativeness',
            'values' : 'work ethic, dedication, self-sacrifice, goal-driven, focus',
            'accomplishment' : 'CEO tesla cars, spaceX, starlinks, billionamire',
            },
        }
#print(mentors)

for role, model in mentors.items():
    print(role)
    for key, value in  model.items():
        print(f"\t{key.title()}~ {value}")
