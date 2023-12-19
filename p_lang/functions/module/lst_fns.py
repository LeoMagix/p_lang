from list_functions import print_models
from list_functions import show_completed_models as scm

unprinted_designs = ['pendant', 'reptile', 'robort']

completed_models = []

print(unprinted_designs)
print(completed_models)

print_models(unprinted_designs, completed_models)

scm(completed_models)

print(unprinted_designs)
print(completed_models)
print()

#To prevent the function from modifying the original list.
    #> function_name(list_name[:])
designs = ['joker', 'batman', 'thanos']

finish = []

print(designs)
print(f'{finish}\n')

print_models(designs[:], finish)
scm(finish)

print(designs)
print(finish)
