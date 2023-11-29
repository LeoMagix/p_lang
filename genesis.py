usr/env/bin/python3

first_day = 'let there be light'
enigma = 'the creator'
genesis = f"And God said, {first_day.upper()}!"

#Practicing the use of strings and f-strings
print(genesis)
print(f"And there was light.")
print(f"You can not fathom {enigma.title()}'s moves.\n")
print(f"Always strive to be better than the previous day.\n")
#Flexing your List
finishers = ['mj23', 'lm10', 'r52', 'ant34']
greats = []

print(finishers)
finishers.insert(-1, 'ub9.58')
print(finishers)
finishers.append('musk')
print(f"{finishers}\n")

#voyage into for loops
brands = ['nike', 'adidas', 'puma']
for shoe in brands:
    print(f"\t{shoe.title()}:")
    print(f"{shoe} is a great sneaker brand.")
    print(f"{shoe.upper()} makes nice shoes.\n")

print(f"{brands[0]} air jordan is the better shoe though.\n") 

clothes = ['nike', 'LV', 'replay']
for trend in clothes:
    print(trend.upper())
print(f"I prefer to wear {clothes[2]}.\n")
for great in finishers:
     print(f"{great.upper()} always performs under pressure.")
     print(f"Be like {great.upper()}.\n")
print('Jesus said, "Use your head"\n')

print("lists of the greats: \n\tMicheal Jordan \n\tLionel Messi \n\tRay Lewis \n\tNikolai Tesla.")

#trying to employ range()
greatness = []
for greats in range(1, 5):
    great = greats **2
    greatness.append(great)
    print(greatness)
