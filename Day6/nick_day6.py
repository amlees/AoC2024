import numpy as np

from copy import deepcopy
from collections import defaultdict

map_dict = {
    ".": 0, # empty
    "#": 1, # blocked
    "X": 2, # visited (not in initial data)
    "^" : 3, # up
    ">" : 4, # right
    "v" : 5, # down
    "<" : 6, # left
}

direction_dict = {
    3 : [-1, 0],
    4 : [0, 1],
    5 : [1, 0],
    6 : [0, -1]
}

map_list = []
with open("day6_input.txt", "r") as fptr:
    while row := fptr.readline():
        map_list.append([map_dict[x] for x in row.strip("\n")])

# Initialize the map and set first direction
map_array = np.array(map_list)
position = np.where(map_array > 2)
direction = map_array[position][0]

start_position = deepcopy(position)
start_direction = deepcopy(direction)

map_array[position] = 2

# Walk the guard around the map
while True:
    position = tuple([x + y for x, y in zip(position, direction_dict[direction])])
    if any([x < 0 or x >= y for x, y in zip(position, (map_array.shape))]):
        break # guard has exited the map
    if map_array[position] == 1:
        # Blocked - reverse position and change direction
        position = tuple([x - y for x, y in zip(position, direction_dict[direction])])
        direction = (direction - 2) % 4 + 3
    else:
        map_array[position] = 2

print(f"Part One Answer: {np.sum(map_array == 2)}")


def test_map(map_array, start_position, start_direction) -> bool:
    is_loop = False

    position = deepcopy(start_position)
    direction = deepcopy(start_direction)
    
    history = defaultdict(int)
    while True:
        position = tuple([x + y for x, y in zip(position, direction_dict[direction])])
        if any([x < 0 or x >= y for x, y in zip(position, (map_array.shape))]):
            break # guard has exited the map
        if map_array[position] == 1:
            # Blocked - reverse position and change direction
            history[f"{int(position[0]),int(position[1]),direction}"] += 1
            if history[f"{int(position[0]),int(position[1]),direction}"] > 1:
                is_loop = True
                break
            else:
                position = tuple([x - y for x, y in zip(position, direction_dict[direction])])
                direction = (direction - 2) % 4 + 3

    return is_loop

possible_positions = np.where(map_array == 2)

position = deepcopy(start_position)
direction = deepcopy(start_direction)

ind = []
for row_ind, col_ind in zip(possible_positions[0], possible_positions[1]):
    print(f"Test {row_ind}, {col_ind}")
    map_array[row_ind, col_ind] = 1
    is_loop = test_map(map_array, position, direction)
    if is_loop:
        ind.append((row_ind, col_ind))
        print(ind)
    map_array[row_ind, col_ind] = 0

print(f"Part Two Answer: {len(ind)}")