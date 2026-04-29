"""Program to practise simple manipulation of list"""

pillars  = ['honesty', 'integrity', 'attitude', 'discipline']

for pillar in range(len(pillars)):
    if pillar == len(pillars) - 1:
        print('and ' + pillars[pillar].upper())
        break
    print(pillars[pillar].upper(), end=", ")
