import time

from BFS import BFS
from sokoban import clear
from sokoban_map import find_robot_pos, find_can_pos, print_game_state, find_goal_pos


def solve(maze):
    clear()

    all_cans = find_can_pos(maze)
    robot_pos = find_robot_pos(maze)
    goal_pos = find_goal_pos(maze)
    print_game_state(maze)

    start_time = time.time()
    print('Beginning search!')
    print('Robot Position:', robot_pos)
    print('Can positions:', all_cans)
    print('Goal positions:', goal_pos)
    print()

    if len(all_cans) < len(goal_pos):
        print('Unsolvable.')
        return -1, 0

    try:
        # path = BFS(maze, robot_pos, all_cans, goal_pos, [(robot_pos, all_cans)])
        path, explored_states = BFS(maze, robot_pos, all_cans, goal_pos, (robot_pos, ))
        print()
        print(path)
        print('Path length:', len(path))
        solve_time = (time.time() - start_time)
        print("--- %s seconds ---" % solve_time)
        return solve_time, explored_states
    except KeyboardInterrupt as e:
        return -2, 0

# solve(game_state)

