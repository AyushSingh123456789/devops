# List-to-Dictionary Loot Conversion

# Imagine that the same fantasy video game represents a vanquished dragon’s loot as a list of strings, like this:

# dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


# Write a function named add_to_inventory(inventory, added_items). The inventory parameter is a dictionary representing the player’s inventory (as in the previous project) and the added_items parameter is a list, like dragon_loot. The add_to_inventory() function should return a dictionary that represents the player’s updated inventory. Note that the added_items list can contain multiples of the same item. Your code could look something like this:


def add_to_inventory(inventory, added_items):
    for item in added_items:
       inventory[item] = inventory.get(item,0)+1
    return inventory
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
print(inv)


#inventory.get(item, 0) looks up the current item in the dictionary. If the item already exists, it returns its current count. If it does not exist yet, it safely returns 0 instead of crashing with a KeyError
#+ 1 adds 1 to that count (either incrementing an existing item or turning the 0 into 1 for a brand-new item).
#inventory[item] = ... assigns that new updated count back to the item key in the dictionary.


# The previous program (with your display_inventory() function from the previous project) would output the following:

# Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger

# Total number of items: 48