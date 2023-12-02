#program to calculaye BMI
weight = int(input('Please enter weight in kg - '))
height = float(input('Please enter height in meters - '))
BMI = int(weight // height ** 2)
print('Your BMI is' + ' ' + str(BMI) + 'kg/m^2')
