#Program for group admin
usr_names = input('Enter usernames: ').split()
print(usr_names)
for user in usr_names:
    if user == 'admin':
        print('Hello admin! Welcome on board. You want status report?')
    
    elif user != 'admin':
        print(f'Hello {user}, welcome onboard.')

    else:
        if usr_names == []:
            print('We need new users ASAP!')
print('\n')

new_usrs = input().split()
for new in new_usrs:
    if new.lower() in usr_names:
        print('Sorry, username is not available.')
    
    else:
        print(f'{new}, thanks for logging on.')
