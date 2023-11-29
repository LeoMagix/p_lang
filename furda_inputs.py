#Exploring user interactions even further.
#1.Car rental:
#print("WELCOME TO IJENI'S CAR RENTAL!!!")
#print()
#rent = input('What kind of car are you looking for?\n')
#avail_cars = ['ferrrari', 'xzibit', 'porsche', 'lexus']
#print()
#print('Please wait while we search your car...')
#print()
#if rent in avail_cars:
    #print(f'{rent} is available.')
    #print('Enjoy Your Drive!')
    #print()
#elif rent not in avail_cars:
    #print("Sorry, your car of choice is not available for rent.")
    #print('List of Available Cars:')
    #for avail in avail_cars:
        #print(f'\t{avail}')
    #print()
#print("THANKS FOR DRIVING WITH US.")
print('\n')

#2.Restaurant Table Order:
#diner = input("Would you like to make diner reservations?\nyes or no\n")
#print('\n')

#if diner == 'yes':
    #print("Welcome to MaMa put's Diner.")
    #print()
    
    #diners = 'To help us serve you adequately, please enter the number of persons.\n'
    #diners += 'This is a table reservation for? - '
    #num = input(diners)
    #num = int(num)
    #print()

    #if num < 8:
        #print("You can make your dinner reservations...")
        #print('\t Your table is ready!')
    
    #elif num >= 8:
        #print("Sorry, you may have to wait to get a table.")
        #print("Apologies for the inconvienience.")

#else:
    #print('Oops!!!')
#print()

#3.H.C.M
print("This is a program to determine the multiples of 10.")
multiple = int(input('Enter a Number:\n '))
print()

if multiple % 10 == 0:
    print(f"{multiple} is a multiple of 10.")
else:
    print(f"{multiple} is not a multiple of 10.")

