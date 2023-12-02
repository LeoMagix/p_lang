def describe_city(city, country):
    """Return a City and a Country."""
    describe = f'"{city.title()}, {country.title()}"'
    
    return describe

city1 = describe_city('san francisco', 'u.s.a')

city2 = describe_city('rosario', 'argentina')

city3 = describe_city('akwa ibom', 'nigeria')

print(city1)
print(city2)
print(city3)
