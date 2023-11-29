#Understanding while loops.
#count = 0                   #baseline/initial point for comparison.
#while count <= 10:          #control of the loop
    #count += 1              #terminator of the loop/ end point
    #print(f'{count}. no')
#print()

#c = 100
#while c > 10:           #To avoid infinity loops, don't create conditions that are always True in the program.
    #c += 1                  #Starting your loop with a false condition won't give an output:
    #if c == 200:                    # c = 100; while c > 10 - this is always going to be true through out the life of the program.
        #break                       # c = 10; while c > 10 - this is false.
    #print(c)

#count = 0
#while count <= 5:
    #print(count, end = ' ')
    #count += 1
    #print(count)

#gbas is the flag
gbas = 20
while gbas:
    for i in range(gbas + 1):
        count = i + 1
        if count == gbas:
            gbas = False
            print("end of line")
        else:
            print(count)
print()
'''
gbos = 20
while gbos:
    count = 1
    count *= 2
    if count == gbos:
        gbos = False
        break
    
    else:
        print(count)
'''
