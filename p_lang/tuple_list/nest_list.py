"""
nested = [23, 34, 24, ['nole', 'greek freak', 'black mamba'], 10, 11]
print(nested[0])
print(nested[1])
print(nested[3])
print(f"The length of our list is {len(nested)}.")
print(f'{nested[3][2]}\n')

for nest in nested[3]:
    print(nest)
print()

for nests in nested:
    if nests is nested[3]:
        for nam in nests:
            print(nam)
    else:
        print(nests)
"""
#student1-9,8,8,4
#student2-10,2,4,6
#student3-5,6,10,8
#student4-10,10,8,6
twoDlist = [[9,8,8,4], [10,2,4,6], [5,6,10,8], [10,10,8,6]]
print(twoDlist[0])
print(twoDlist[-1])
print(twoDlist[2])
print(f"The length of our 2D list is {len(twoDlist)}.\n")

print(twoDlist[2][0:2])
print(twoDlist[3][ :3])
print(twoDlist[1][2: ])
print(twoDlist[0][0:1])
print(twoDlist[2][0])
print(twoDlist[1][1])
print()

pos = twoDlist[3].index(8)
print(pos)
print()

for scores in twoDlist:
    for score in scores:
        print(score, end=' ')
    print()
