#Creating a Class of Users
class User:
    """This will create a class of different users."""
    
    def __init__(self, first, last, middle=''):
        "Initialize an instance of different users."
        
        self.first = first
        
        self.last = last
        
        self.middle = middle
    
    def user_info(self):
        """
        writes the provided information by the user.
        Prints the user details in a neat format.
        """
        
        #full_name = f"{self.first} {self.last}"
        
        #print(full_name)
        
        if self.middle != '':
            full_name = f"{self.first} {self.middle} {self.last}"
            print(full_name)
        
        else:
            full_name = f"{self.first} {self.last}"
            print(full_name)
    
    def describe_user(self):
        """Just basic info about our user."""
        full_name = f"{self.first} {self.middle} {self.last}"
        desc = f"My name is {full_name.title()}.\n"
        desc += "And I am a Fullstack Software Engineer."
        return desc
    
    def greet_user(self):
        """Felicitate with the user."""
        guy = f'{self.last.title()}.'
        print('Hello' + ' ' + guy)

user = User('david', 'leonard')

user.user_info()
print(user.describe_user())
user.greet_user()
print()
bio = User('david','adah','leonard')
bio.user_info()
print(bio.describe_user())
bio.greet_user()
