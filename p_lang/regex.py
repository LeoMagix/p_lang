"""Practice file for simple intro to Regular expressions(Regex)"""
import re

ph = re.compile(r'(\d{,3})[-,](\d{3})[-,](\d{3})')

nom = ph.search('the goal number 100,000,000 & $300-000-000')
print(nom.group())
print(nom.group(1), nom.group(3))
print(nom.groups())
print(ph.findall("Monthly pay:100,000,000 Net worth:500,000,000,000"))

print()
phoneNo = re.compile(r'(\+234 \d{,4}|\d{2,3}\d) (\d{3} \d{4})')
chek = phoneNo.search('Dads Number: 0803 598 0455')
print(chek.group())
print(chek.groups())
ps = phoneNo.findall("Old contact:0806 677 4370 New contact:+234 806 703 1285")
print(ps)

print()
alte = phoneNo.search('Mums Num; +234 707 963 3311')
print(alte.group())
print(alte.groups())

print()
tdk = re.compile(r'Bat(wo)*man')
bat = tdk.search("find Batwowowowoman")
print(bat.group())

print()
ball = re.compile(r'Air\sJordan', re.I)
baller = ball.findall("Michael air jordan, Air jordan. AIR JORDAN")
print(baller)
#print(baller.groups())     #Can't call the group() and groups() method when findall is involved

numsRegex = re.compile(r'\d+')
print(numsRegex.sub('X', '6 rings, 5 mvps, 6 fmvps, 2 golds, 1 dpoy, 1 ncaa'))

#Match all numbers with a comma after three(3) numbers
numbas = re.compile(r'\d{1,3}(,\d{3})*?')
numRegex = numbas.findall('Search 4,234 and 1,234,456 and 42')
print(numRegex)

#Another attempt
nameRegex = re.compile('^([A-Z])\w+ Nakamoto$')
names = nameRegex.findall('Satoshi Nakamoto, Alice Nakamoto')
print(names)

#Try again
match = re.compile(r'(Alice|Bob|Carol) (eats|throws|pets) (Apples|Cats|Baseballs)', re.I)
matchRegex = match.findall('Alice eats Apples, Bob pets Cats, Robocop throws baseballs')
print(matchRegex)
