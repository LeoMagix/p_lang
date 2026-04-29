"""
A new way to mess with 
strings in python.

"""
#print(object(s), end=End, sep=Separator, file=File, flush=Flush)
print("hardwork pays dividends")
print("learning is ", end = ' ')
print('power\n', end = '')
print("God is the greatest")
print("Excellence always seduces success")
print("Welcome to", end = '@')
print("newday", end = '\n')
print("codingGuru", sep = '')
print('18','05','2023', sep = '/')
print('Dah', 'CodingGuru', sep ='@')
s = 'a'+'bc'
print(s)

#input()
nom = input("\nPlease, enter name: ")
print(nom)
print('Data Type', type(nom))

num = input("enter number: ")
print(num)
print("type of num", type(num))

#script to convert user input from string to other data types#
digit = int(input("\nEnter serial pin: "))
print(digit)
print("specify data type\n", type(digit))

#script to take separated input in one line#
print("Enter a two(2) word greeting")
a, s = input('Greetings!: ').split()            #using the spilt() function
print(a, s, sep="||")

x,y = input('Enter Two(2) Digits:').split()            #x,y or x, y either is feasible
print(x,y, sep=",")
print("type of x", type(x))
print("type of y", type(y))

print('\nGive me 2 numbers')
w,z = input().split()
print(w,z, sep="||")
print("what's ur type w", type(int(w)))
print("what's ur type z", type(int(z)))

a = int(input("\nEnter value for a:"))      #let's do maths
b = int(input("Enter value for b:"))
c = a + b
print(a)
print(b)
print('The sum of a, b is ', c)

print("\nValue of a")
a = int(input())
print("Value of b")
b = float(input())
c = a + b
print('The value of c: ', c)
