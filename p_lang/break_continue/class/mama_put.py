#First Class in Class:
class Mama_put:
    """Creation of instances of mama put."""
    
    def __init__(self, restaurant_name, cuisine_name):
        """Initialize the restaurant name and cuisine attributes of the mama put."""
        
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name

    def describe_mama_put(self):
        """
        Print the restaurant's name and the cuisine they serve,
        and in a neat format.
        """
        
        print(f"Welcome to {self.restaurant_name.upper()}'s mama put.")
        
        print(f"And we serve a special {self.cuisine_name.title()} cuisine.\n")

    def open_mama_put(self, location):
        """ Declare that the restaurant is open."""
        
        print(f"Yay!!! {self.restaurant_name.title()} is now open.")
        print(f"we are located at {location.title()}.")

kpancakey = Mama_put('kpankaky', 'pancake')

print(kpancakey.restaurant_name) 

print(kpancakey.cuisine_name)

print()

kpancakey.describe_mama_put()

kpancakey.open_mama_put('abuja')

print()

restaurant = Mama_put("mama's kitchen", 'african dish')

restaurant.describe_mama_put()

restaurant.open_mama_put('calabar')
