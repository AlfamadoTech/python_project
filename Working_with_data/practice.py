first_trees = [1, 2, 3, 4, 5]

tree_list = list(range(20, 141, 4))
print(tree_list)

tree_list.append(400)
print(tree_list)

old_trees = [500, 600, 700]
combined_trees = tree_list + old_trees
print(combined_trees)

conifers = ["Pine", "Fir", "Juniper"]
cycads = ["Cycas", "Sago palm", "Zamia"]
# gymnosperms = [conifers, cycads]
# print(gymnosperms)

# print(gymnosperms[1][0:2])

ordered_plant = conifers + cycads
ordered_plant.sort()
print(ordered_plant)
