def smelt_ore(inventory):
    inventory[1] = "Iron Bar" if inventory[1] == "Iron Ore" else inventory[1]

    return inventory
