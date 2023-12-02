#program to interact with pizza customer
pizza = input('What kind of pizza do you want? ')
price = 0

if pizza == 'small':
    price = 10
    print(f'price of small pizza is {price}')
elif pizza == 'medium':
    price = 20
    print(f'price of medium pizza is {price}')
else:
    price = 50
    print(f'price of large pizza is {price}')

perr = input('Would you like a pepperroni? ')
if perr == 'yes' or perr == 'YES':
    if pizza == 'small':
        price = price + 30
        print(f'price of pizza is {price}')
    else:
        if pizza == 'medium' or pizza == 'large':
            price = price + 50
            print(f'price is {price}')

    extra = input('you want extra cheese? ')
    if extra == 'yes':
        price = price + 20
        print(f'{price}')
