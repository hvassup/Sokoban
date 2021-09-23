from collections import deque

from sokoban import is_success, state_to_states

MAX_DEPTH = 500


# BFS which finds the first path that solves the game
def BFS(maze, current_robot_pos, current_all_cans, all_goals, path):
    queue = deque([])
    queue.append((current_robot_pos, current_all_cans, path))

    all_goals_list = list(all_goals)
    explored_states = 0
    while len(queue) > 0:
        explored_states = explored_states + 1
        current_robot_pos, current_all_cans, path = queue.popleft()

        if is_success(all_goals_list, current_all_cans):
            print('Done! :)')
            return path, explored_states

        if len(path) > MAX_DEPTH:
            raise Exception('Max search depth reached')

        states = state_to_states(current_robot_pos, current_all_cans, maze)
        for next_robot_pos, next_all_cans in states:
            new_path = path + (next_robot_pos,)
            queue.append((next_robot_pos, next_all_cans, new_path))

    print('Oops', path)
    return 'Oops', explored_states
