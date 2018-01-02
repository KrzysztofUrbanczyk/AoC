import numpy as np

with open('input') as f:
    _input = list(map(lambda line: list(line), f.read().splitlines()))

array = np.array(_input)

N, S, W, E = (-1, 0), (1, 0), (0, -1), (0, 1)
turn_left = {N: W, W: S, S: E, E: N}
turn_right = {N: E, E: S, S: W, W: N}
forward = {N: N, W: W, S: S, E: E}
backward = {N: S, E: W, S: N, W: E}

x, y = len(array[0]) // 2, len(array) // 2

dx, dy = N

for _ in range(200):
    array = np.insert(array, len(array), '.', axis=1)
    array = np.insert(array, len(array), '.', axis=0)
    array = np.insert(array, 0, '.', axis=1)
    array = np.insert(array, 0, '.', axis=0)

x, y = len(array[0]) // 2, len(array) // 2

result = 0
for _ in range(10000000):
    if array[x, y] == '.':
        array[x, y] = 'W'
        tmp_x, tmp_y = turn_left[dx, dy]
        x, y = x + tmp_x, y + tmp_y
        dx, dy = tmp_x, tmp_y
    elif array[x, y] == 'W':
        result += 1
        array[x, y] = '#'
        tmp_x, tmp_y = forward[dx, dy]
        x, y = x + tmp_x, y + tmp_y
        dx, dy = tmp_x, tmp_y
    elif array[x, y] == '#':
        array[x, y] = 'F'
        tmp_x, tmp_y = turn_right[dx, dy]
        x, y = x + tmp_x, y + tmp_y
        dx, dy = tmp_x, tmp_y
    elif array[x, y] == 'F':
        array[x, y] = '.'
        tmp_x, tmp_y = backward[dx, dy]
        x, y = x + tmp_x, y + tmp_y
        dx, dy = tmp_x, tmp_y

print(result)
