#Coin toss program
import random

coin = input("head's or tail's:  ")
toss = random.randint(0, 1)
#print(toss)

if toss == 0:
    print("Head")

else:
    print('Tail')
