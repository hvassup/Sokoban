import random

from brain import solve
from sokoban_map import string_map_to_state


def file_to_maps():
    re_maps = {}
    current_map_name = ''
    with open('sokevo.txt') as f:
        for line in f.readlines():
            line = line.rstrip('\n')
            if line.startswith('#'):
                re_maps[current_map_name].append(list(line))
            elif line.startswith(';'):
                current_map_name = line
                re_maps[current_map_name] = []
    return re_maps


maps = file_to_maps()
results = []

shuffled_keys = list(maps.keys())
random.shuffle(shuffled_keys)
for k in shuffled_keys:
    if k not in ['; Tara Gelson']:  # '; Samantha Gelson']:W
        continue
    print('Running on maze:', k)
    maze = string_map_to_state(maps[k])
    solve_time, explored_states = solve(maze)
    results.append((k, solve_time))

    with open('results.txt', 'a') as f:
        f.write(f'{k}\t{solve_time}\t{explored_states}\n')

print('####')
print('Final results:')
for k in results:
    print(k)
