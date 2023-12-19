"""This is a program to pass a list as a parameter to a function."""

'''
#Start with some designs that need to be printed
unprinted_designs = ['phone case', 'pendant', 'robot']
completed_models = []

#Simulate printing each design until none is left
#move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing Model: {current_design}")
    completed_models.append(current_design)

#Display all completed models
print("The following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
'''

#The same program optimsed more efficiently using a function
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        print(f"Printing model: {current_design}")
        
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all models that were printed."""
    print("The following models have been printed:")
    
    for completed_model in completed_models:
        print(completed_model)
