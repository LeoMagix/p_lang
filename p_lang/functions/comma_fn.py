"""
A simple function that takes a list as an argument, prints each item of the list
followed by a comma and a blank space, then an 'and' with a blank space before the last item
in the list.
"""

#Function comma_lst  has parameter lst_val
def comma_lst(lst_val):
    """
    Receives a list value, prints each followed by a comma and space.
    Before printing the last item instead of a comma an "and" and a space.
    """
    # Loops through the length of the list- using the list index to output the list items
    # Check if itera == len(lst-val) - 1; if true perform the required operation
    # and exit the loop.
    for itera in range(len(lst_val)):
        item = lst_val[itera]
        # Conditional statement to manipulate last list item
        if itera == len(lst_val) - 1:
            item = lst_val[itera]
            print(f"and {item}")
            break
        print(f"{item}", end=", ")

fruits = ['banana', 'apple', 'pineapple', 'orange', 'mango']
comma_lst(fruits)

men_dem = ['My Father', 'Nikola Tesla', 'Richard Feynman', 'Michael Jordan', 'Myles Munroe', 'Rema']
comma_lst(men_dem)
