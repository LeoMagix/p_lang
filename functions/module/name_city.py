import city_fn

city1 = city_fn.describe_city('rosario', 'argentina')
drury = f"The little boy from {city1} is a world champion."
print(drury)

site = city_fn.describe_city('rome', 'italy')
print(f"{site}, is an awesome site to behold")
