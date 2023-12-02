wt = int(input('WEIGHT: '))
ht = float(input('HEIGHT: '))
bmi  = round(wt / ht**2, 1)

print(bmi)
if bmi < 16.0:
    print('u need to chop food')
    if bmi > 16.0 and bmi <= 16.9:
        print('u still de lean')
        if bmi > 17.0 and bmi <= 18.4:
            print('underweight ne!')
elif bmi >= 18.5 and bmi <= 24.9:
    print('guy you fit die')
elif bmi >= 25.0 and bmi <= 29.9:
    print('u don de fat o')
else:
    if bmi >= 30.0 and bmi <=34.9:
        print('fat human')
    elif bmi >= 35.0 and bmi <= 39.9:
        print('fatty bumbum')
    elif bmi >= 40:
        print('obese baby')
