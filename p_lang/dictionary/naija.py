#Testing my understanding of creating a multiline Python dictionary.

nation = {
        'continent':'africa',
        'country' : 'nigeria',
        'capital' : 'abuja',
        'colonial masters' : 'British',
        'independent' : 'october 1st, 1960',
        'Geographical area' : 'west africa',
        'Geographical size' : '9.2million sqm',
        'language(s)' : 'Idoma, Igbo, Yoruba, Hausa, ...500+',
        'ethnicity' : 'Over 740 ethnic groups',
        }
print(f'{nation}\n')

nation['states']='36 states'
nation['religion(s)']='atheists, paganism, christianity, islam'
nation['ethnicity']='700+ ethnic groups'

for data, info in nation.items():
        print(f"{data.upper()}:")
        print(f"\t{info.title()}")
        print()
