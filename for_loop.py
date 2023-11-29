#for i in range(10):
    #print(i)
#print(f'\n{i + 1}')

#for i in list(range(1, 21, 2)):
        #print(i, end = ' ')
        #i = i ** 2
        #print(i)
#print('Did it work?')

'''
vals = [1,2,3,4,4,5,6]
for t in vals:
    print(t)
    vals.append(t * 2)          #creates an infinite iteration/loop
print(vals)
print(sum(vals))
'''

#lst = []
#for x in range(12+1):
    #lst.append(x * 2)
    #print(lst)
    #print(max(lst))
#print(f'\n{lst}')
#print(sum(lst))

#strs = ['effort', 'work', 'resilience']
#for word in strs:
    #print(strs)
    #print(f'{word} is the answer')
    #print(word.upper() + ' ' + 'leads to excellence\n')
#print(type(word))
#print(word[0:5])

#program to calculate interest for given principals
stPrin = 500
endPrin = 550
r = 10
t = 5
#for p in range(stPrin, endPrin + 1, 2):
    #I = int((p * r * t) / 100)
    #print(p, end = '  ')
    #print(I)
#print(I)

#ans = int(input())
#for l in range(ans + 1):
    #ans += l
    #print(ans)

#mpty = input().split()
#print(mpty)
#for leta in mpty:
    #print(leta)


gamers = ['sky', 'rocky', 'slinga']
'''
#for no in range(1, len(gamers) + 1):
    #for gamer in gamers:
        #print(gamer)
    #print(no)
'''    
'''
for gamer in gamers:
    for no in range(1, len(gamers) + 1):
        print(no)
    print(gamer)
'''
#col = 4
#for i in range(4):
    #for j in range(col):
        #c = i * col + j
        #print(c, end = ' ')
    #print(i)

lst = [[x for x in range(3)] for y in range(4)]
#print(lst)

