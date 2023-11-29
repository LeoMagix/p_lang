#TEST PROGRAM FOR while LOOP WITH LISTS.

#Start with users that need to be verified,
#and empty lists to hold confirmed users.
unregistered = ['bola', 'friday', 'dan', 'gabu']
registered = []

#Verify each user until there are no more unregistered users,
#then move then to list of registered users.
while unregistered:                     #as long as list is not empty this is true, i.e. == while = True.
    current_user = unregistered.pop()       #This takes care automatically of the possibility of an infinity loop.
    print(f"Verify user: {current_user}")
    registered.append(current_user)

#Display all confirmed users.
print("\nThe following users have been registered:")
for users in registered:
    print(users)
