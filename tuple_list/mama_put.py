#Practicing Tuple in Python.
#selling local dish at a restaurant

dish = ('eba', 'rice', 'kpomo', 'okpa')

print("Welcome to Iya Basira's Local Dish")
while True:
    ans = input('you wan buy food? '  )
    if ans == 'yes' or ans == 'Yes':
        print('Na food weh dey be dis')
        
        for food in dish:
            print(food)
    else:
        print("Toh, bye bye!")
        break

    request = input('Abeg, enter ur choice?: ' ).split()
    print(request)
    for choice in request:
        if choice in dish:
            print(f'ur {choice} is ready!\n')
    
        elif choice not in dish:
            print(f'\nSorry, {choice} no dey')

    print('Na all u want be dat?')
    print('Chow De Go!!\n')
