from utils import inputfile_to_array

map = inputfile_to_array("inputs/input_day_3.txt")

slope_list = [
[1, 1],
[3, 1],
[5, 1],
[7, 1],
[1, 2],
]
def traverse_different_slopes(map,slope_list):
    tree_hits = 1 # Set to 1 because the answer is a product, so setting it to 0 would give 0 either way
    for slope in slope_list:
        current_tree_hits = traverse_slope(map, slope)
        tree_hits = tree_hits * current_tree_hits
    return tree_hits

def traverse_slope(map,slope=[3,1]):
    x = 0
    tree_counter = 0
    width_of_map = len(map[0])
    right_steps = slope[0]
    down_steps = slope[1]
    for y, val in enumerate(map):
        if (y)%down_steps == 0 and y!= 0:
            x = x+right_steps
            if x >= width_of_map:
                x = x - width_of_map
            if val[x] == '#':
                tree_counter = tree_counter + 1
    return tree_counter

print("The number of tree hits in task a are:", traverse_slope(map) )
print("The number of trees hits in task b are:", traverse_different_slopes(map, slope_list) )