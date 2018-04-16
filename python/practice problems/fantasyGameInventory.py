stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
	print('Inventory:')
	itemTotal = 0
	for key, value in inventory.items():
		print(str(value) + ' ' + key)
		itemTotal += value
	print('Total number of items: ' + str(itemTotal))

def addToInventory(inventory, addedItems):
    for loot in addedItems:
    	inventory.setdefault(loot, 0)
    	inventory[loot] = inventory[loot] + 1
#	print(addedItems)

addToInventory(stuff, dragonLoot)
displayInventory(stuff)