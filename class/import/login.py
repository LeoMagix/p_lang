"""Systematically handles user information."""

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
        print(f"login attempt is {user.login_attempts} times.\n")
