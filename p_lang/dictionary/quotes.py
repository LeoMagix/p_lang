"""Writing a program that stores dictionary in a list."""

viking = f'"Odin gave his left eye to acquire knowledge, I will give far more to acquire it."'
ragner = {'ragner lothbrok': viking}

mindset = f'"limits like fears, are often just an illusion."'
mj = {'michael jordan': mindset}

work = f'"Competition is the easy part, the real work happens behind the scenes."'
bolt = {'usain bolt' : work}

# Create a list of dictionaries
great_quotes = [ragner, mj, bolt]
#print(great_quotes)

for greats in great_quotes:
    for great, quotes in sorted(greats.items()):
        print(quotes)
        if great == 'michael jordan':
            #print(f'\t\t\t\t\t-{great.title()}\n')
            print('\t'*5, f"-{great.title()}")
        
        elif great == 'usain bolt':
            #print(f'\t\t\t\t\t\t\t\t-{great.title()}\n')
            print('\t'*8, f"-{great.title()}")
        
        else:
            #print(f'\t\t\t\t\t\t\t\t\t-{great.title()}\n')
            print('\t'*9, f"-{great.title()}")
