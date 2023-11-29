"""Set of classes to neatly deal with Admin privileges."""

from login import User

class CreateGroup:
    """Represents a gruop created by permitted persons."""
    
    def __init__(self, admin_power=''):
        """Initialize attributes and methods for this class."""
        self.admin_powers = admin_power

    def admin_privilege(self):
        """Assigns admin permission to create group."""
        self.admin_power = ['create group', 'add group tags', 'delete group tags']
        print("As an admin, with regards to a group you can:")
        for admin in self.admin_power:
            print(f'*{admin}')

class Admin(User):
    """Creates an administrative user with peculiar permissions."""
    
    def __init__(self, user_name, user_id):
        """Initialize the attributes and methods of the superclass, User."""
        super().__init__(user_name, user_id)
        self.privileges = ''
        self.group = CreateGroup()

    def show_privileges(self):
        """Defines and displays the permissions granted to admin."""
        self.privileges = ['can add post', 'can post video/audio', 'can del post']
        print("List of administrative permissions for the Admin-")
        for priv in self.privileges:
            print(f'-{priv}')
