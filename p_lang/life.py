#program that relates the stage of life
age = int(input())
if age < 2:
    print('tata')
elif age < 4:
    print('toddlers')
elif age < 13:
    print('kids')
elif age < 20:
    print('teenager')
elif age < 65:
    print('adulthood')
elif age >= 65:
    print('aged')
