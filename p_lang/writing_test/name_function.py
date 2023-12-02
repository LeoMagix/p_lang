#Function to practice test code
def get_formatted_name(first, last, middle=''):
    """Get a neatly formatted name."""
    if middle:
        formatted_name = f'{first} {middle} {last}'
        return formatted_name.title()
    
    else:
        formatted_name = f'{first} {last}'
        return formatted_name.title()
