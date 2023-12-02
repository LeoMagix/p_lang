#A program that models a lottery."""

from random import choice

class luck:
    """Created class to simulate a lottery."""
    
    def __init__(self, pick_4=0):
        """Initialize attributes of our lucky class."""
        self.pick_4 = (2, 3, 3, 4, 'j', 'e', 's', 'u', 's', 5, 2,
                1, 0, 2, 4)
        self.ticket = []

    def lottery(self):
        """Randomly pick 4 items, numbers or letters from our tuple.""" 
        trial = ['j', 'e', 2, 3]
        
        cnt = 0
        while True:
            cnt += 1
            seq = 0
            
            while seq < 4:
                game = choice(self.pick_4)
                self.ticket.append(game)
                seq += 1
            
            print(f'\nThis is your {cnt} attempt.')
            print(self.ticket)
            
            if trial == self.ticket:
                print("\nYou finally won!")
                print(f'It took you {cnt} tries to win.')
                break
            
            elif trial != self.ticket:
                del self.ticket[:4]
        

games = luck()
#print(games.ticket)
games.lottery()
#games.test()
