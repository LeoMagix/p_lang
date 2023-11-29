#Designing a love meter
nom1 = input('').lower()
nom2 = input('').lower()
non = nom1.count('t') + nom1.count('r') + nom1.count('u') + nom1.count('e')
nor = nom2.count('t') + nom2.count('r') + nom2.count('u') + nom2.count('e')
non1 = nom1.count('l') + nom1.count('o') + nom1.count('v') + nom1.count('e')
nor1 = nom2.count('l') + nom2.count('o') + nom2.count('v') + nom2.count('e')
tru = nor + non
lov = non1 + nor1
amore = str(tru) + str(lov)
lover_birds = int(amore)


if lover_birds < 10:
    print(f'{amore},you are not compatible')

elif lover_birds < 50 or lovo <= 79:
    print(f'{amore}, it may work')

else:
    if lover_birds >= 90:
        print(f'{amore}, love birds')
print('found ur love yet?')
