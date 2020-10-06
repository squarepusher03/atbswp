inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inv):
    """Displays the inventory dictionary passed."""
    print("Inventory:")
    total_items = 0
    for item in inv.keys():
        total_items += int(inv[item])
        print(inv[item], item)
    print("Total number of items: " + str(total_items))


if __name__ == "__main__":
    display_inventory(inventory)
