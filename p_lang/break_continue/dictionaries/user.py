#Testing User Input For Dictionaries.
#user1 = input('What is first name?\n ')
#user2 = input('Enter last name please-\n ')
#user = {'first name' : user1, 'last name' : user2,}
#print(user)
#for data, info in user.items():
    #print(f'{data.upper()} - {info.title()}')
    #print()

#Student Data.
fname = input('Enter first name\n')
lname = input('Enter last name\n')
faculty = input('Enter faculty\n')
dept = input('Enter name of department\n')
reg_no = input("What's your registration number?\n")
level = input("What's your level?\n")

data = {
        'first name' : fname,
        'last name' : lname,
        'faculty' : faculty,
        'department' : dept,
        'registration number' : str(reg_no),
        'level' : str(level),
       }
#print(data)
print('\n')
print('STUDENT PROFILE:')
for stu, info in data.items():
    if stu == 'registration number':
        if len(info) == 9:
            print(f'\t{stu.title()}: {info.title()}')
        
        elif len(info) < 9 or len(info) > 9:
            print("Enter valid registration number.")
    else:
        print(f'\t{stu.title()}: {info.title()}')
    print()
