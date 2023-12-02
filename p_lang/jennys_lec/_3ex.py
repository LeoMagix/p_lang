#basic program to add strings
'''
no1 = input()
no2 = input()
sum = no1 + no2
add = int(no1) + int(no2)
print(sum)
print(add)
print('\n')
'''
"""
num = input("Please enter two digits: ")
print(num[0] + num[1])
print(int(num[0]) + int(num[1]))
"""
weight = int(input('Please weight in kg - '))
height = float(input('Please enter height in meter - '))
BMI = weight / height**2
bmi = round(BMI, 2)
print("BMI is" + ' ' + str(bmi) + 'kg/m^2')
