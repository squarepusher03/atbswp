from rpg_inventory import display_inventory


def add_to_inventory(inventory, added_items):
    """Adds passed items to the inventory

    Keyword arguments:
    inventory -- the inventory of the player
    addedItems -- the items being added to the player's inventory
    """
    for key in added_items:
        if key not in inventory:
            inventory.setdefault(key, 1)
        else:
            inventory[key] += 1

    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
