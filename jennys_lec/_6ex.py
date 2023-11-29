#program to check if a number is even or odd
'''
num = int(input('Enter number: '))
if num % 2 == 0:
    print(f'{num} is Even')
else:
    print(f'{num} is Odd')
'''
#program to determine height limit and price in a theme park
height = int(input("Please enter height in feet- "))
bill = 0

if height > 3:
    print('Welcome to Grossland Park')
    
    age = int(input('Oga, Enter your age: '))
    if age >= 5 and age <= 15:
        bill = 10
        print(f'your money na {bill}bucks')
    
    elif age >= 16 and age <= 20 :
        bill = 20
        print(f'your money na {bill}bucks')
    
    elif age > 20:
        bill = 200
        print(f'your money na {bill}bucks')
    
    else:
        print('Go Home!')
    
    photo = input('you go snap picture(yes/no)?  ')
    if photo == 'yes' or photo == 'Yes':
        bill = bill + 20
        print(f'ur total money na {bill}bucks')

else:
    print('Sorry, You can\'t ride')
print('Thank you for patronising Grossland')
