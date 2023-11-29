avail_soups = ['afang', 'egusi', 'banga', 'okoro', 'okoho']
common_soups = []
avail_soups += ['okoro', 'banga', 'banga', 'ogbono']

for soups in avail_soups:
    print(soups)
print()

while 'banga' in avail_soups:
    avail_soups.remove('banga')
    print(avail_soups)
    print()

while avail_soups:
    soup = avail_soups.pop()
    print(f"We have prepared {soup.title()}.")
    common_soups.append(soup)
print()

for common in common_soups:
    print(f"{common.title()} is a common soup in Nigeria.")

