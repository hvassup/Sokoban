from sokoban import get_coord_diff, get_neighbours
from sokoban_map import find_can_pos

int_to_str = {
     0: 'UP',
     1: 'RIGHT',
     2: 'DOWN',
     3: 'LEFT',
}

test_path = [((1, 1), [(3, 3), (3, 5), (3, 7)]), ((1, 2), [(3, 3), (3, 5), (3, 7)]), ((1, 3), [(3, 3), (3, 5), (3, 7)]), ((1, 4), [(3, 3), (3, 5), (3, 7)]), ((1, 5), [(3, 3), (3, 5), (3, 7)]), ((1, 6), [(3, 3), (3, 5), (3, 7)]), ((1, 7), [(3, 3), (3, 5), (3, 7)]), ((2, 7), [(3, 3), (3, 5), (3, 7)]), ((3, 7), [(3, 3), (3, 5), (4, 7)]), ((4, 7), [(3, 3), (3, 5), (5, 7)]), ((5, 7), [(3, 3), (3, 5), (6, 7)]), ((6, 7), [(3, 3), (3, 5), (7, 7)]), ((5, 7), [(3, 3), (3, 5), (7, 7)]), ((5, 6), [(3, 3), (3, 5), (7, 7)]), ((5, 5), [(3, 3), (3, 5), 
(7, 7)]), ((4, 5), [(3, 3), (3, 5), (7, 7)]), ((3, 5), [(3, 3), (2, 5), (7, 7)]), ((2, 5), [(3, 3), (1, 5), (7, 7)]), ((3, 5), [(3, 3), (1, 5), (7, 7)]), ((3, 4), [(3, 3), (1, 5), (7, 7)]), ((3, 3), [(3, 2), (1, 5), (7, 7)]), ((3, 2), [(3, 1), (1, 5), (7, 7)]), ((3, 3), [(3, 1), (1, 5), (7, 7)]), ((2, 3), [(3, 1), (1, 5), (7, 7)]), ((1, 3), [(3, 1), (1, 5), (7, 7)]), ((1, 2), [(3, 1), (1, 5), (7, 7)]), ((1, 1), [(3, 1), (1, 5), (7, 7)]), ((2, 1), [(3, 1), (1, 5), (7, 7)]), ((3, 1), [(4, 1), (1, 5), (7, 7)]), ((4, 1), [(5, 1), (1, 5), (7, 7)]), ((5, 1), [(6, 1), (1, 5), (7, 7)]), ((6, 1), [(7, 1), (1, 5), (7, 7)])]

def diff_to_direction(diff_x, diff_y):
    if diff_x == -1:
        return 3
    elif diff_x == 1:
        return 1
    elif diff_y == -1:
        return 0
    elif diff_y == 1:
        return 2

def direction_deg_diff(dir1, dir2):
    turn_angle = (dir1 - dir2) * -90
    if turn_angle == 270:
        return -90
    return turn_angle

def is_pathway(coord):
    x, y = coord
    neighbours = get_neighbours(x, y)
    if len(neighbours) == 2:
        if neighbours[0][0] == neighbours[1][0] or  neighbours[0][1] == neighbours[1][1]:
            return True
    return False
    

def path_to_instructions(_path):
    path, cans_path = list(zip(*_path))

    print(path)
    previous_direction = direction = diff_to_direction(path[0][0], path[0][1])
    instructions = []

    for i in range(1, len(path)):
        diff_x, diff_y = get_coord_diff(path[i], path[i - 1])
        direction = diff_to_direction(diff_x, diff_y)
        
        deg_to_rotate = direction_deg_diff(previous_direction, direction)
        
        previous_direction = direction
        #print(path[i], cans_path[i])
        if cans_path[i] != cans_path[i - 1]:
            is_pushing_can = True
        else:
            is_pushing_can = False
        # print(int_to_str[direction], deg_to_rotate, is_pathway(path[i - 1]), is_pushing_can)
        
        instructions.append((direction, deg_to_rotate, is_pathway(path[i - 1]), is_pushing_can))
    return instructions


def get_test_path():
    return path_to_instructions(test_path)
