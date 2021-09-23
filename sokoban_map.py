# Map from assignment
string_map = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', '@', ' ', ' ', ' ', ' ', ' ', '.', 'X'],
    ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
    ['X', ' ', ' ', '$', ' ', ' ', ' ', ' ', 'X'],
    ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
    ['X', '.', ' ', '$', ' ', ' ', ' ', ' ', 'X'],
    ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
    ['X', ' ', ' ', '$', ' ', ' ', ' ', '.', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]

state_to_str = {
    0: ' ',
    1: '@',
    2: 'X',
    3: '.',
    4: '$',
    5: '*',
}

str_to_state = {
    ' ': 0,  # BLANK
    '@': 1,  # ROBOT
    '+': 1,  # ROBOT
    'X': 2,  # WALL
    '#': 2,  # WALL
    '.': 3,  # GOAL
    '$': 4,  # CAN
    '*': 5,  # CAN ON GOAL
}


def string_map_to_state(maze):
    return [[str_to_state[y] for y in x] for x in maze]


game_state = string_map_to_state(string_map)


# Finds something in the map
def find_type_pos(maze, func):
    positions = set()
    map_dim = max(len(maze), len(maze[0]))
    for y in range(0, map_dim):
        for x in range(0, map_dim):
            try:
                if func(maze[y][x]):
                    positions.add((x, y))
            except:
                pass
    return positions


# Finds robot position in the game state
def find_robot_pos(maze):
    return find_type_pos(maze, lambda block: block == 1).pop()


# Finds can position in the game state
def find_can_pos(maze):
    return find_type_pos(maze, lambda block: block == 4 or block == 5)


# Finds can position in the game state
def find_goal_pos(maze):
    return find_type_pos(maze, lambda block: block == 3 or block == 5)


# Visualise game state
def print_game_state(maze):
    for i in maze:
        for state in i:
            print(state_to_str[state], end='')
        print()
