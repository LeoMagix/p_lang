class Dog:
    def __init__(self, name, age):
        """Initialize's dog name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('willie', 5)
print(f"My dog's name is {my_dog.name}.")
print(f"And it is {my_dog.age} years old.")
print()
my_dog.sit()
my_dog.roll_over()

my_dog = Dog('pikachu', 5)
print(f"My dog's name is {my_dog.name}.")
print(f"And it is {my_dog.age} years old.")
print()
my_dog.sit()
my_dog.roll_over()
