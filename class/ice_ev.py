#LEARNING TO SHARE THE INHERITANCE OF A PARENT CLASS AND ITS CHILD CLASS.
class Car:
    
    def __init__(self, make, model, year):
        """Initialize attributes for a simple car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive_name."""
        motor_name = f"{self.year} {self.make} {self.model}"
        return motor_name.title()

    def read_odometer(self):
        """Print a statement showing car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Update odometer through a method.
        Set the odometer reading to the given value.
        """
        #self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back an Odometer reading.")

    def increment_odometer(self, miles):
        """Add given value to the odometer reading."""
        self.odometer_reading += miles
   
    def gas_tank(self):
        """Information on the volume of gas tank."""
        car = f"{self.make}, {self.model}"
        print(f"{car}, has a gas tank of ...ltr.")
#Creating an instance from an attribute
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
        '''Initializes attributes of the superclass Car.'''
        super().__init__(make, model, year)
        #self.battery_size = 75
        self.battery = Battery()
    '''
    def describe_battery(self):
        """Prints statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")
    '''
    def gas_tank(self):
        """Overriding a method of the superclass."""
        print("This car doesn't use gas.")
     

ev = ElectricCar('tesla', 'cybertruck', '2020')
print(ev.get_descriptive_name())
#ev.describe_battery()
ev.gas_tank()
ev.battery.describe_battery()
ev.battery.get_range()
ev.battery.upgrade_battery()
ev.battery.get_range()
