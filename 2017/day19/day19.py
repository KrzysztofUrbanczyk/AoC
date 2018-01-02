import numpy as np

with open('input') as f:
    _input = list(map(lambda line: list(line), f.read().splitlines()))

routing_diagram = np.array(_input)
for line in routing_diagram:
    if len(line) < 201:
        line.extend([' '] * (201 - len(line)))

N, S, W, E = (-1, 0), (1, 0), (0, -1), (0, 1)
forward = {N: N, W: W, S: S, E: E}
possible_direction = {N: [E, W], S: [E, W], E: [N, S], W: [N, S]}


x, y = 0, routing_diagram[0].index('|')
dx, dy = S

result = ''
steps = 0

while True:
    if routing_diagram[x][y] == '+':
        steps += 1
        zz = possible_direction[dx, dy]
        for key in zz:
            poss_x, poss_y = key
            new_x, new_y = x + poss_x, y + poss_y
            char = routing_diagram[new_x][new_y]
            if (char == '|' and (key == S or key == N)) or (char == '-' and (key == E or key == W)):
                x, y = new_x, new_y
                dx, dy = key
                end = False
                break
    else:
        if routing_diagram[x][y].isalpha():
            result += routing_diagram[x][y]

        tmp_x, tmp_y = forward[dx, dy]
        x, y = x + tmp_x, y + tmp_y
        dx, dy = tmp_x, tmp_y
        steps += 1
        if routing_diagram[x][y] == ' ':
            break

#part 1
print(result)

#part 2
print(steps)