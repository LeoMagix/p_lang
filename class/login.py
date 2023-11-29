class User:
    """Build a class of required user information."""
    def __init__(self, user_name, user_id):
        """Initialises simple attributes of the user details."""
        self.user_name = user_name
        self.user_id = user_id
        self.login_attempts = 0

    def req_login_info(self):
        """
        Enquires if user is a member.
        Prompts user to enter user details to login.
        """
        print("If you are a registered member, please enter user name and user id.")
        print(f"USERNAME:{self.user_name.title()}")
        print(f"USER ID:{self.user_id.upper()}")

    def increment_login_attempts(self):
        """Increase login attempts by 1."""
        self.login_attempts += 1
        #print(self.login_attempts)
    
    def reset_login_attempts(self):
        """A method to reset users attempted login to 0 on 3 attempts."""
        if self.login_attempts >= 3:
            self.login_attempts *= 0

    def info_login_attempts(self):
        """Inform user on login attempts."""
        print(f"{self.user_name.upper()}, attempted login:{self.login_attempts}...")

user  = User('jumpman23', '6fmvp5mvp')
user.req_login_info()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
user.info_login_attempts()
print(f"login attempt is {user.login_attempts} times.\n")

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

hall_admin = Admin('balance', 'fulfudefinest')
hall_admin.req_login_info()
hall_admin.show_privileges()
hall_admin.group.admin_privilege()
