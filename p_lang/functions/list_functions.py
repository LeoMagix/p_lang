#Working with Lists in a Function.
def greet_users(lst):
    """Passing a list to a function."""
    
    for name in lst:
        msgs = f"Hello! {name.title()}"
        print(msgs)

names = ['jidenna', 'prizmo', 'ibikun']

greet_users(names)
print('\n')

#>Modifying a list in a function:
'''
#Start with some designs that need to be printed
unprinted_designs = ['phone case', 'pendant', 'robort']
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
#>Here's the same program optimsed more efficiently using a function
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

unprinted_designs = ['pendant', 'reptile', 'robort']

completed_models = []

print(unprinted_designs)
print(completed_models)

print_models(unprinted_designs, completed_models)

show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)
print()

#Stopping the function from modifying the original list.
#> function_name(list_name[:])
designs = ['joker', 'batman', 'thanos']

finish = []

print(designs)
print(f'{finish}\n')

print_models(designs[:], finish)

show_completed_models(finish)

print(designs)
print(finish)
