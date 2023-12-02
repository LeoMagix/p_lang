greats = []
greats.append('mj23')
greats.insert(1, 'nikola tesla')
greats.insert(0, 'mj23')
greats.insert(2, 'zara hadid')
greats.insert(-2, 'elon musk')
swags = ['nike', 'adidas', 'new balance', 'versace']
#test = greats[<index>] $#     #dis one de accepted#

#FOR LOOPS
print(greats)
del greats[1]
print(f'{greats}\n')

for great in greats:
    print(great)       #dis one too de work just 4 fun, but u neva kno#
    print(f'Be inspired by greatness')
    print(f'{great.upper()}, an image of God')
    print(f'{great.title()}', "The Goat!\n")

for swagu in swags:
    print(swagu)
    print(f'Making a Statement?\n')
        #for swagu in swags:...         #tried it, didn't work#
            #print(swagu)##

magicians = ['houldini', 'messi', 'kyrie', 'mahomes']
print('MAGICIANS\t')
for magician in magicians:
    print(f'\t{magician.title()}')
print(f'{magicians[1]} is a beast tho\n')

#numbas = [0, 1, 2, 4, 6, 8, 10]...
#print(numbas)
#for x in numbas:
    #y = x + 2
    #numbas.append(y)
#...print(numbas)##
#x = 10...
#for i >= 10 in x:
    #x = x + 2
    #...print(x)##       #Well that didn't go as planned#

#The 'range()' Function
for value in range(1,5):        #range() can only be used to print a list of numbers...I think?#
    print(value)
print('\n')

for val in range(6):
    print(val)
print('\n')

outs = list(range(2, 8))        #list() passes the values/numbas from range() into a list# 
print(outs)

skips = list(range(1, 10, 3))   
print(skips)
#for value in skips:...
    #skip = value * 2   #didn't work#
    #skips.append(skip)
#...print(skips)##
print('\n')

sums = []
for add in range(2,10):
    print(add)
    calc = add + 2
    sums.append(calc)
    print(sums)
print('\n')
print(sums)
print('\n')

muls = []
for times in range(10):
    muls.append(times * 3)
    print(muls)
print('\n')
print(muls)
print('\n')

squares = [value**2 for value in range(1, 11)]          #foray into "list comprehensions"#
print(squares)
print('\n')

div = [quotient / 2 for quotient in range(1, 20, 2)]
print(div)
print('\n')

digits = [0, 1, 2, 3, 4, 5, 6]
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))
print('\n')

tr = list(range(7))
print(tr)
for val in tr:
    tri  = val + 2
    print(tri)
print(tr)
