#Foray into Function continues.
def T_shirts(size='xxl', message='i love python'):
    """Customizing t-shirts message."""
    print(f"Shirt size is {size.upper()}:")
    
    print(f'The message on size {size.upper()} should read, "{message.title()}"')
    
    print("You like.")
    
    print()

T_shirts('lx')

T_shirts(message='pressure is earned')

T_shirts('xx', "you can't teach this.")

T_shirts('xl', 'the blacker the berry, the bigger i shoot.')    #> positional arguments

T_shirts(size='l', message='class is permanent.')             #> keyword arguments

T_shirts(message="the god of impossibilty.", size='c')      #> keyword arguments

T_shirts()
