import numpy as np

with open('input') as f:
    _input = list(map(lambda line: list(line), f.read().splitlines()))

array = np.array(_input)

N, S, W, E = (-1, 0), (1, 0), (0, -1), (0, 1)
turn_left = {N: W, W: S, S: E, E: N}
turn_right = {N: E, E: S, S: W, W: N}

x, y = len(array[0]) // 2, len(array) // 2

dx, dy = N

for _ in range(400):
    array = np.insert(array, len(array), '.', axis=1)
    array = np.insert(array, len(array), '.', axis=0)
    array = np.insert(array, 0, '.', axis=1)
    array = np.insert(array, 0, '.', axis=0)

x, y = len(array[0]) // 2, len(array) // 2

result = 0
for _ in range(10000):
    if array[x, y] == '.':
        result += 1
        array[x, y] = '#'
        tmp_x, tmp_y = turn_left[dx, dy]
        x, y = x + tmp_x, y + tmp_y
        dx, dy = tmp_x, tmp_y
    else:
        array[x, y] = '.'
        tmp_x, tmp_y = turn_right[dx, dy]
        x, y = x + tmp_x, y + tmp_y
        dx, dy = tmp_x, tmp_y

print(result)
