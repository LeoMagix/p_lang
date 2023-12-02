#comprehending list comprehensions
#> [expression for loop]

#squares = [value**2 for value in range(1, 10, 2)]
#print(squares)

#odd = [x for x in range(1, 20, 2)]
#print(odd)

#even = [e for e in range(0, 20, 2)]
#print(even)

#cubes = [trois ** 3 for trois in range(0, 20)]
#print(cubes)

#trois = [tre * 3 for tre in range(0, 10)]
#print(trois)

#nest = [[x for x in range(5)] for j in range(5)]
#print(nest )

#line separated input:
#n = int(input())
#nest = [[int(c) for c in input().split()] for r in range(n)]
#print(nest)
#print('\n')

#space separated input:
row = int(input('No. of rows '))
col = int(input('No. of columns '))
twoD = input().split()
matrix = [[int(twoD[i * col + j]) for j in range(col)] for i in range(row)] 
print(matrix)
print()

for rows in matrix:
    for col in rows:
        print(col, end=' ')
    print()
'''
nest = [[2,1,2], [3,2,1], [4,1,9], [0,0,1]]
for row in nest:
    #print(row)
    for col in row:
        print(col, end = ', ')
    print() 
    #print(row)

print('Matrix!')
#print(nest[3][0:2])
print(nest[0:3][2])
print(nest[0:3])
print(nest[0][2])
'''
