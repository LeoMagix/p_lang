class Car:
    def __init__(self, make, model, year):
        """Initialize attributes for a simple car."""
        self.make = make
        self.model = model
        self.year = year
    #>Setting default values for an attribute.
        self.odometer_reading = 0       

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive_name."""
        motor_name = f"{self.year} {self.make} {self.model}"
        return motor_name.title()
    
    def read_odometer(self):
        """Print a statement showing car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
#Modifying an attributes value
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

new_car = Car('audi', 'a4', 2019)
print(new_car.get_descriptive_name())
new_car.read_odometer()
print(new_car.odometer_reading)
new_car.odometer_reading=23     #>modifying an attribute directly
new_car.read_odometer()
new_car.update_odometer(24)
new_car.read_odometer()
new_car.update_odometer(-2)
new_car.read_odometer()
print()

car_used = Car('ferrari', '54-italia', 2020)
print(car_used.get_descriptive_name())
car_used.update_odometer(2300)
car_used.read_odometer()
car_used.increment_odometer(500)
car_used.read_odometer()
