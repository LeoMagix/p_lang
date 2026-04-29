"""Program simulates taking stock of inventory of a fantasy game."""

inventory = {'rope':1, 'gold chain':12, 'dagger':42, 'arrow':6, 'bazooka':23, 'torch':7}

def display_inv(inv):
    """Displays a neat presentation of the inventory."""
    total = 0

    print("Inventory:")
    for k, v in inv.items():
        print(f"{v} {k}")
        total += v
    
    print(f"Total Inventory: {total}")


display_inv(inventory)
print()

dragonloot = ['gold chain', 'dagger', 'gold chain', 'ruby']

def add_to_inv(dic_inv, add_items):
    """Add a list of items to the inventory dictionary."""
    for i in add_items:
        if i in dic_inv:
            dic_inv[i] += 1
        else:
            dic_inv[i] = 1
    return dic_inv


dic = add_to_inv(inventory, dragonloot)
print(dic)
display_inv(inventory)
