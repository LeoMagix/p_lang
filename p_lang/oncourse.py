#MESSING WITH STRINGS
guru = 'I just too sabi'
word = "No be by how far, na by how well"
lucky = 23
message = "Hello Pythonistas!"
name = f"The name is David, and I am KING!"
identity = f'The demi-god'
first_name = 'extra'
last_name = 'ordinary'

print(message)
print(name)
print(identity)
#print(identity!)##
print(f"{guru}")            #format string (f-strings) application#
print(f'{word}!\n')
print(f"{name} Call me {identity}\n")
print(f'{message} {identity} is here.\nFavorite number,{lucky} if you need to get lucky.\n')
print(f'{guru.upper()} guy.\n')                 #applying methods: upper(),lower(),title() etc.# 
print(f"First name {first_name.title()}, last name {last_name.upper()}!\n")
print(f'{message.lower()}\n')
print(f'{first_name.upper()} no de {last_name.upper()}!\n')
#Manipulating Whitespaces in Python
print(f"Personal Data:\n{message}\n\t {name}\n\t {identity}\n\t {guru}!!!\n")
print(f"GOD's IMAGE:\n\t King David\n\t Saint Augustine\n\t Michael Jordan\n\t Nikola Tesla\n\t Elon Musk\n\t Zara Hadid\n")

dad = "Mr.Sunday Adah, my father is the closest image to God for me. "
mum = " My mum, Mrs.Agnes Ogiri Adah is nothing but an inspiration."
parent = " I am favoured by God to have such great parents. "
        
print(f'{dad}')         #experimenting with strip(), rstrip(), and lstrip() methods#
print(f'{mum}')
print(f'{parent}\n')
print(f"{dad.rstrip()}")    #3*strip() methods only temporarily eliminate whitespaces#
print(f"{mum.lstrip()}")
print(f"{parent.strip()}\n")

dad = dad.strip()
parent = parent.strip()
spirit = '"go dominate!"'

print(dad)
print(f'{parent.upper()}\n')
print(f'Jesus said, "Use your head"\n')
print(f"God's instruction to me was {spirit.upper()}\n")
#Other Data Types
floats = 3.0 + 12.325
integer = 12 + 23
flo = 10 / 3

print(floats)
print(integer)
print(12.30 / 4)
print(23 + 34 * 2 - 3**3)
print(2.5 % 2)
print(2.5 / 2)
print(0.75 * 2)
print(flo)
print(4 / 2)
print(32 / 2**4)

x, y, z = 12, 23, 4             #flexing multiple assignment#

print(x + y)
print(y * z)
print(f'{x + y + z}')

x, y, z = 'show', 'me ur', 32

print(f'\n{x}')
print(y)
print(z)
print(f'{x.title()} {y} {z} o!\n')
#The declaration#
print(f"I AM:\n\tGod's Image\n\tKing\n\tDemi-god\n\tThe Head\n\tDominant\n\tCompetitive")
print(f"\tHard working\n\tHumble\n\tSuccessful\n\tThe Best\n\tComplete\n\tDestined\t")
print(f'\tObsessed with Greatness\n')
#BIG GUNS:LIST
super_cars = ['ferrari', 'porsche', 'bugatti', 'lambogini', 'stan']
cars = ['tesla', 'stan', 'mercedes benz', "lexus", "rolls royce"]
best_minds = ["micheal jordan", "nikola tesla", "elon musk", "zara hadid"]
#black_cat = f'{best_minds[0]}, {air jordan.upper()}')##
black_cat = f'{best_minds[0].title()}, Air Jordan, flight 23' 

print(super_cars)
print(cars)
print(f'{best_minds}\n')
print('Length of Elements in my List')
print(len(super_cars))
print(len(cars))
print(len(best_minds))
print(f"\n{super_cars}")
print(super_cars[0])                #using index to obtain a precise element/item in a list#
print(f"The favorite items in my lists I want to belive are:\n\t1.{super_cars[1].upper()}\n\t2.{cars[3].upper()}\n\t3.{best_minds[-4].upper()}")
print(f'His Airness, {best_minds[0].title()}.')
print(black_cat)
print(f'\n{best_minds[0].title()}, dominance, a perfect demonstration of the beauty and power of a positively competitive mind.')
print(f'{best_minds[1].title()}, god of electricity, beauty of a creative mind, proof that there is no limit to what the mind can produce.')
print(f'{best_minds[2].title()}, trail blazer, ultimate perfection of resourcefulness and productivity.')
print(f'{best_minds[3].title()}, "queen of curves", trend setter in a profession not too accomodating at the time.')
print(f"\nHmmmm... fast cars {super_cars[0]}, {super_cars[1]}, {super_cars[2]}, {super_cars[3]}, {super_cars[4]}. I love it!")
print(f'Favorite Cars:\n\t {cars[0].title()}\n\t {cars[1].title()}\n\t {cars[3].title()}\n\t {cars[2].title()}\n\t {cars[4].title()}')
#Modifying the Elements in the List
print(f'\n{cars}')

cars[2] = 'chevrolet'       #replacing an item with another#
flashy = cars[3]
ice = cars
print(cars)
print(f'\n{flashy}')
print (f'\n{ice}')                 #this syntax of print() works also#

ice[2] = 'lucid'
print(ice)
print(f'\n{cars}')
print(f'\n{super_cars}')

cars.append('mercedes benz')        #rising of append() methods#
super_cars.append('pegani')
evs = []
evs.append('tesla plaid')
evs.append('tesla cybertruck')
evs.append('lucid')
evs.append('hyundai ioniq')

#print('\ncars)
#print(\nsuper_cars)#               
#print(\nevs)##

print(evs)
#flashy.insert(1, 'pegani')##       #methods no dey work for variables#

ice.insert(-1, 'cyber truck')
evs.insert(-1, 'tesla semi')
print(f'\n{ice}')
print(f'{evs}\n')

goats = ['mj23', 'lm10', 'ub9.58', 'ray52', 'lbj', 'cr7', 'federer']
print(goats)

#goats.insert('tb12')##
goats.insert(-1,'tb12')
print(goats)
#removing elements from list#
del goats[-2]                   #del statement go comot items permanently#
print(goats)

goats.append('tb12')
print(goats)

nfl = goats.pop()               #pop() go remov item/element frm ur list com store am for anoda variable to use later#
print(f'\n{nfl}')                   #just pop() go work with d last item for ur lists#
print(goats)
print(f'{nfl.title()}, Mr.7superbowls\n')

snd_best = goats.pop(-2)            #pop(2), dat is with d index e go comot d element com store for anoda variable# 
print(snd_best)
print(f'{snd_best.upper()}, the guy de try sha.')
print(goats)

leGm = goats.pop(-2)
print(f'\n{leGm}')
print(f"King james, {leGm.upper()}; it's not how you begin but how you arrive")
print(goats)

#cars = goats.pop()##                   #u no fit pop into a list and...
#print(f'\n{super_cars.title()}')##     #if u pop new item into same variable e go take d data of d new value#

print(f'\n{super_cars}')
super_cars.remove('pegani')             #remove() methods, wen u no fit remember the index/positon of the item but you know the name#
print(super_cars)

print(f'\n{ice}')
not_ice = 'tesla'
ice.remove(not_ice)                     #na anoda way to use remove() methods#
print(ice)
print(f'{not_ice.title()} motors inc is a trail blazer in non ICE cars.\n')

ice.append('stan')
print(ice)
ice.remove('stan')                          #for repeated items in a list, remove() takes care only of the 1st occurence#
print(ice)

ice.remove('cyber truck')                   #extra care if u de pass a list as value 4 anoda variable cos anytin weh u do...
                                            #one variable go affect the other exactly#
print(f'\n{super_cars}')
print(cars)
print(goats)
print(ice)
print(evs)
print(best_minds)

cars.sort()                             #reorganise your list chronologically with the sort() methods#
(super_cars.sort())                         #sort() go permanently rearrange d list#
ice.sort(reverse=True)                      #reverse order too dey#

print(f'\n{super_cars}')
print(cars)
print(goats)
#print(goats.sort())?#                  #NONE?#     
print(ice)

print(f'\n{sorted(evs)}')               #sorted() methods, temporary rearrangement for the win#
print(evs)
print(f'\n{best_minds}')
print(sorted(best_minds))
print(sorted(best_minds, reverse=True))
print(best_minds)
#print(sorted(reverse=True, best_minds))##

print(f'\n{goats}')
print(sorted(goats, reverse=True))
#print(goats.reverse())?#               #NONE?#
goats.reverse()
print(f'{goats}\n')
#print(f'{goats.upper()}')##

women_force = ['zara hadid', 'magaret hamilton']
women_force[1]='margaret elaine hamilton' 
women_force.append('shelly ann fraser-pryce')
women_force.insert(0, 'Agnes Angela Adah')
women_force.append('rihanna the mogul')
women_force.append('marie curie')
women_force.insert(2, 'margot robbie')
women_force.append('cinderella')

print(f'{women_force}\n')
print(sorted(women_force))
print(sorted(women_force, reverse=True))
print(f'{women_force}\n')

women_force.sort()
print(women_force)

women_force.sort(reverse=True)
print(women_force)

women_force.reverse()
print(f'{women_force}\n')

del women_force[1]
women_force.remove('margot robbie')
fenty = women_force.pop(3)              #if u de use pop() check ur prev line of code make u no go confuse urself# 
print(women_force)
print(f'I prefer {fenty} to the singer.\n')

#bones_jones = []...
#for victim in bones_jones:
    #bones_jones.append('daniel cormier')
    #bones_jones.append('shogun rua')
    #bones_jones.append('lyoto machida')
    #bones_jones.append('ciryl gane')
    #...print(bones_jones)##
"""
testing a new way to
write out multiple line 
comments
"""

'''
well done sir,
it works
'''
#Some important functions working with LISTS
"""
append()    >> list_name.append(<value>) ; value == a 'string', number, variable
extend()    >> list_name.extend([<value>] ;
remove()    >> list_name.remove(<value>]
pop()       >> list_name.pop(); last item or list.name.pop(<[index]>)
insert()    >> list_name.insert(<index>, <value>)
index()     >> list_name.index(<item>)
sort()      >> list_name.sort() ; sort(reverse=True)
sorted()    >> sorted(list_name); sorted(lst, reverse=True); sorted(lst, key=str.lower)
reverse()   >> list_name.reverse()
len()       >> len(<var>)
range()     >> range(start, end, step)
list()      >> list(<value>)
min()       >> min(<var>)
max()       >> max(<var>)
sum()       >> sum(<var>)
