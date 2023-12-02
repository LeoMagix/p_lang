#program to calculate number of years on until 90years
age = int(input(f"Enter current age:  "))
"""
    1 year = 365 days
    1 year = 52 weeks
    1 year = 12 months
"""
x90_days = 32850
y90_wks = 4680
z90_months = 1080

xage_days = 365 * age
yage_wks = 52 * age
zage_months = 12 * age

a = x90_days - xage_days
b = y90_wks - yage_wks
c = z90_months  - zage_months
print(f'You have {a} days, {b} weeks and {c} months left')
