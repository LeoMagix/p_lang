"""Let's create a simple dictionary."""

bio = f"personal profile"

data = {"First Name" : "David", "Middle Name" : "leonard", "Last Name":"Adah"}
print(data)

print(f'{bio.upper()}:')
for key in data:
    print(key)
print()

for value in data.values():
    if value == 'Adah':
        print(value)
        print('\n')
    else:
        print(value)


for key, value in data.items():
    print(f"*{key.upper()}- {value.title()}")
print()

data['nationality']='nigerian'
data['profession']='fullstack engineer'
data['languages']='idoma, hausa, english, french, spanish, italian, japanese'
data['net worth']='500 Billion'
print(data)
print()

bio2 = f"updated personal profile"
print(f"{bio2.upper()}:")

 for info, file in data.items():
    print(f"\t{info.upper()}-{file.title()}")
