'''
text = 'welcome to london nigga'
txt = text.split(" ")       #creates a list
print(txt)
'''
#progran to randomly select who pays amongst peers
import random

pals = input('Enter names of peers: ').split()       #or split(",")
nom_no = len(pals)
who_pays = random.randrange(0, nom_no)
the_one = pals[who_pays]
print(pals)

print(f'{the_one} is paying our bills')
