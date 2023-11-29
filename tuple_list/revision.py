#Practice Program To re-familiarise myself with Python list.
big3 = []
nole = 'Novak Djokovic'
rafa = 'Rafael Nadal'
roger = 'Roger Federer'

big3.append(rafa)
big3.extend([roger])
big3.insert(0, nole)
print(big3)
print()

big3[1] = roger
del big3[2]
big3 += [rafa]
print(big3)
print()
#position = big3.index(nole)
#print(position)
oo1 = big3[0]
stat =f'{oo1} has the most tennis grand slams with 24.'
stat += ' And the most titles in major tournaments'
print(stat)

clay = big3[2]
roland = f"{clay}, called 'The King of Clay' has won 14 Roland Garros. "
roland += "The most french open titles."
print(roland)

swiss = big3[1]
print(f"{swiss}, the swiss maestro won 20 grand slams in tennis.")

big3+=['Andy Murray']
big4 = big3[0:]
print(len(big3))
print(big4)
andy = big3.pop()
print(f"Though a great tennis player, {andy} is not a part of the 'big 3'.")
print()
print("These are the 'big 3';")
for three in big3:
    print(f'\t-{three}')
