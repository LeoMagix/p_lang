
#l, b = input().split()
#L = int(l)
#B = int(b)
#print(L*B)


#nom  = input()
#age = int(input())
#print("The name of the person is", nom, end = ' ')
#print('and the age is', age, end = '.')
#print('\n')

#sf = int(input())
#ef = int(input())
#w = int(input())
#for f in range(sf, ef + 1, w):
    #cel = (32 * f - 32) * 5 / 9
    #print(f'{f}\t {cel}')

#n = int(input())
#print('\n')
#if n > 0: 
    #for i in range(1, n+1):
        #print(i, end = ' ')
        #if i % 2 == 0:
            #print(i)    #u no fit use 'return' outside a function
        
            #continue
        #elif i % 2 != 0 and n / i == 1:
                #print(i)
        
        #else:
            #print(0)

usrs = ['sky', 'rocket', 'betty']
for user in usrs:
    print(user)

new_usr = input('Enter user name - ')
if new_usr not in usrs:
    usrs.append(new_usr)
    for new in usrs:
        print(f'\n{new}')

elif new_usr in usrs:
    print('Username taken')
