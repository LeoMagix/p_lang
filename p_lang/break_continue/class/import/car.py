"""Represents a car."""

class Car:
    """Set of class to represent a simple car."""
    
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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back an Odometer reading.")

    def increment_odometer(self, miles):
        """Add given value to the odometer reading."""
        self.odometer_reading += miles
