"""Writing a program that stores dictionary in a list."""

viking = f'"Odin gave his left eye to acquire knowledge, I will give far more to acquire it."'
ragner = {'ragner lothbrok': viking}

mindset = f'"limits like fears, are often just an illusion."'
mj = {'michael jordan': mindset}

work = f'"Competition is the easy part, the real work happens behind the scenes."'
bolt = {'usain bolt' : work}

great_quotes = [ragner, mj, bolt]
#print(great_quotes)

for greats in great_quotes:
    for great, quotes in sorted(greats.items()):
        print(quotes)
        if great == 'michael jordan':
            print(f'\t\t\t\t\t-{great.title()}\n')
        
        elif great == 'usain bolt':
            print(f'\t\t\t\t\t\t\t\t-{great.title()}\n')
        
        else:
            print(f'\t\t\t\t\t\t\t\t\t-{great.title()}\n')
