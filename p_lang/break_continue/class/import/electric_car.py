from car import Car  

"""Class for the modelling of an EV."""
class Battery:
    """A simple attempt to model a battery for an EV."""
    
    def __init__(self, battery_size = 75):
        """Initializes battery's attribute."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Prints statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """Print statement about the range of the battery."""
        if self.battery_size == 75:
            range = 260
        
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.""")

    def upgrade_battery(self):
        """Upgrades the lowest current battery capacity to 100."""
        if self.battery_size <= 75:
            self.battery_size = 100
            print(f"The battery  size is now {self.battery_size}kwh.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to Electric vehicles(EVs)."""

    def __init__(self, make, model, year):
        """Initializes attributes of the superclass Car."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def gas_tank(self):
        """Overriding a method of the superclass."""
        print("This car doesn't use gas.")
