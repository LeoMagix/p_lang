#program to determine a leap year
yr = int(input('Enter a Year - '))

if yr % 4 == 0 and yr != round(yr, -2):
    print(f"{yr} is a leap year")
    
elif yr == round(yr, -2):
    if yr % 400 == 0:
        print(f'{yr} is a leap year')    
    else:
        print(f'{yr} is not a leap year')

else:
    print(f'{yr} is not a leap year, bye')
