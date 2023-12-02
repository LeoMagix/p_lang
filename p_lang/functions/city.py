def city(name, country= 'afganistan'):
    print(f"Oga {name.title()}, where you wan go? {country.title()}?")

city('driver')
city('yelewa', 'niger')
city(name= 'brukunu')

voyage = city('slimi', 'congo')     #prints this
'''
print(voyage)       #prints None for this.
'''
