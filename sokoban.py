def is_succes(all_goals, all_cans):
    for goal in all_goals:
        if goal not in all_cans:
            return False
    return True

def is_wall(maze, x, y):
    if len(maze) <= y or len(maze[y]) <= x:
        return True
    return maze[y][x] == 2
    
def is_goal(maze, x, y):
    if len(maze) < y or len(maze[y]) < x:
        return True
    return maze[y][x] == 3 or maze[y][x] == 5

def is_corner(maze, x, y):
    neighbor_coords = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
    wall_neighbors = list(filter(lambda i: is_wall(maze, i[0], i[1]), neighbor_coords))
    if len(wall_neighbors) == 3:
        return True
    if len(wall_neighbors) == 2:
        if wall_neighbors[0][0] != wall_neighbors[1][0] and wall_neighbors[0][1] != wall_neighbors[1][1]:
            return True
    return False

def get_coord_diff(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    diff_x = x1 - x2
    diff_y = y1 - y2

    return diff_x, diff_y

def get_next_can_position(robot_pos, can_pos):
    can_x, can_y = can_pos

    diff_x, diff_y = get_coord_diff(can_pos, robot_pos)
    
    x, y = can_x + diff_x, can_y + diff_y
    return x, y

# Check if the robot can move the can 
def can_push_can(maze, robot_pos, can_pos, all_cans):
    x, y = get_next_can_position(robot_pos, can_pos)
    
    if not is_goal(maze, x, y):
        if is_corner(maze, x, y):
            return False
    
    return maze[y][x] != 2 and (x, y) not in all_cans

# Gets neighbour coordinates and filters out illegal moves, returns valid robot moves
def get_neighbours(maze, x, y):
    neighbor_coords = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
    neighbors = list(filter(lambda i: not is_wall(maze, i[0], i[1]), neighbor_coords))
    return neighbors


def filter_moves(maze, x, y, neighbors, all_cans):
    valid_neighbors = []
    for can_x, can_y in neighbors:
        if (can_x, can_y) in all_cans:
            if can_push_can(maze, (x, y), (can_x, can_y), all_cans):
                valid_neighbors.append((can_x, can_y))
        else:
            valid_neighbors.append((can_x, can_y))
    return valid_neighbors

def get_possible_robot_moves(maze, all_cans, robot_pos):
    x, y = robot_pos
    moves = get_neighbours(maze, x, y)
    filtered_moves = filter_moves(maze, x, y, moves, all_cans)
    return filtered_moves

def perform_action(robot_pos, to_coord, all_cans):
    to_x, to_y = to_coord
    new_all_cans = set(all_cans)
  
    if to_coord in new_all_cans:
        to_can_pos = get_next_can_position(robot_pos, to_coord)
        new_all_cans.remove(to_coord)
        new_all_cans.add(to_can_pos)
    
    robot_pos = to_coord

    return robot_pos, new_all_cans

def clear():
    global previous_state_map
    previous_state_map = set()

# Check that the robot is not repeating moves (optimize speed/memory)
previous_state_map = set()
def filter_previous_states(next_states):
    filtered_states = []
    for robot_position, can_positions in next_states:
        state_lookup = (robot_position, ) + tuple(can_positions)
        if state_lookup not in previous_state_map:
            filtered_states.append((robot_position, can_positions))
            previous_state_map.add(state_lookup)
    
    return filtered_states

# Gets the current state and robot position and returns the next possible states
def state_to_states(robot_pos, all_cans, state):
    moves = get_possible_robot_moves(state, all_cans, robot_pos)
    states = [perform_action(robot_pos, next_pos, all_cans) for next_pos in moves]
    filtered_states = filter_previous_states(states)
    
    return filtered_states