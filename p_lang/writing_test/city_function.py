def city_name(city, country, population=0):
    """Neat format of a city and the country."""
    if population:
        name = f"{city.title()}, {country.title()} -population {population}"
        return name
    
    else:
        name = f"{city}, {country}"
        return name.title()
