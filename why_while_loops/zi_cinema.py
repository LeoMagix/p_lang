#Ticket Master
age = "Please enter your age.\n"
age += "'quit' to exit: "

#msg = " "
#while msg != 'quit':
flag = True
while flag:
    msg = input(age)
    print()
    if msg == '':
        #break
        continue
    
    if msg == 'quit':
        flag = False
        print('Goodbye')
    
    elif msg != 'quit':
        age_grade = int(msg)
        if age_grade < 3:
            print("Hurray!! Your ticket is free!")
            print()
        elif age_grade <= 12:
            price = 10
            print(f"Ticket price is {price}$.")
            print()
        elif age_grade <= 90:
            price = 15
            print(f"Ticket Price: {price}$.")
            print()

        if age_grade > 90:
            flag = False
            print("Too old.")
    
