flag = True
while flag:
    print("Please enter a user name.\n")
    usr = input('')
    
    if usr != 'q':
        with open('guest_book.txt', 'a') as guests:
            guests.write('Welcome to my coding exhibition.\n')
            guests.write(f"It's nice to have you on board, {usr}\n")
    

    elif usr == 'q':
        break
        #flag = False
