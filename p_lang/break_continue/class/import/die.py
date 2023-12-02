#Simple rolling of the die."""
import random

class Die:
    """Simulates a die."""

    def __init__(self, sides=6):
        """Initialize attribute and method for our die."""
        self.sides = sides
    
    def roll_dice(self):
        """Rolls the die."""
        roll_num = 10
        roll = 0
        while roll < roll_num:
            play  = random.randint(1, self.sides)
            print(play)
            roll += 1
            print(f"This is die roll number {roll}.\n")
        #roll = random.randint(1, self.sides)
        #print(roll)

alies = Die()
print(f"This is a {alies.sides}-side die.\n")
alies.roll_dice()
