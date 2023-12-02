#RE-INTRODUCTION INTO FUNCTION:
def hello_user():
    """Program to greet the user."""
    print("Hello! And welcome.")

hello_user()

def salute_user(name):
    """Greet the user by name."""   
    print(f"Hello {name.title()}, and welcome!")

salute_user('elsa')

def greet_user(name, work):
    """Let's the user introduce themselves fully.""" 
    info = f"My name is {name.title()} and I'm a {work.title()}."
    return info

desc = greet_user('elsa clares', 'project manager')
print(desc)

bio = greet_user(work='virtual assistant', name='lisa adah')
print(bio)
print()

def user_bio(first, last, middle=''):
    """
    Request the users fullname.
    And then prints it in a neat format.
    """
    fullname = f"{first.title()} {middle.title()} {last.title()}."
    print("The name of our current user:")
    return fullname

desc = user_bio('Elizabeth', 'adah')
print(f'\t{desc}')

info = user_bio(first='elizabeth', last='adah', middle='clares')
print(f'\t{info}')

