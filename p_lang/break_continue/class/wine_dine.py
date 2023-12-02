class Diner:
    def __init__(self, diner_name, cuisine):
        """Iniatialises attributes of the Diner class."""
        self.diner_name = diner_name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_diner(self):
        """
        Displays the name of the restaurant.
        Also gives info on the type of cuisines it serves.
        """
        print(f"Welcome to {self.diner_name.upper()}.")
        print(f"We serve the most exquisite {self.cuisine.title()}.")

    def open_diner(self):
        """Declare the restaurant open for business."""
        yay = f'{self.diner_name.upper()}'
        print(f'{yay} is now...Open!!!')
    
    def set_number_served(self, customer_no):
        """Provide information on the amount of people served."""
        self.number_served = customer_no

    def increment_number_served(self, daily_customers):
        """The amount of people served per day at wine&dine diner."""
        self.number_served += daily_customers

    def giv_update(self):
        """Message to update the number of customers served."""
        print(f"The number of customers served is {self.number_served}.")

foodie = Diner('wine&dine', 'african dishes')
foodie.describe_diner()
foodie.open_diner()
foodie.set_number_served(2)
foodie.increment_number_served(3)
foodie.giv_update()
print('\n')

class IceCreamStand(Diner):
    """Creates a class representing a ice cream spot."""
    
    def __init__(self, diner_name, cuisine):
        """Initializes the attributes and methods of the parent, Diner."""
        super().__init__(diner_name, cuisine)
        self.flavors = ['chocolata', 'vanilla ice', 'creamy ecstacy']

    def display_flavors(self):
        """Print the list of flavors available."""
        print("Come taste our yummy icey creamy flavors:")
        for flavor in self.flavors:
            print(f'\t{flavor}')

    def add_flavor(self):
        """Increase the available flavour choices."""
        self.flavors.append('honey blast')

icy_cream = IceCreamStand('chillax spot', 'ice creams')
icy_cream.describe_diner()
icy_cream.display_flavors()
icy_cream.add_flavor()
icy_cream.display_flavors()
