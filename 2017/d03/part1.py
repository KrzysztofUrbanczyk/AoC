from math import sqrt, fabs
from decimal import Decimal, ROUND_HALF_UP

_input = 368078

N, S, W, E = (1, 0), (-1, 0), (0, -1), (0, 1)
turn_left = {N: W, W: S, S: E, E: N}


def prepare_spiral(_input):
    value = int(Decimal(sqrt(_input)).quantize(0, ROUND_HALF_UP))
    x, y = value // 2, value // 2
    init_x, init_y = x, y
    array = [[None] * (value + 1) for _ in range(value + 1)]
    count = 1
    array[x][y] = count
    dx, dy = E

    while True:
        count += 1
        tmp_x, tmp_y = turn_left[dx, dy]
        new_x, new_y = x + tmp_x, y + tmp_y
        if array[new_x][new_y] is None:
            x, y = new_x, new_y
            dx, dy = tmp_x, tmp_y
        else:
            x, y = x + dx, y + dy
        array[x][y] = count

        if count == _input:
            return int((fabs(init_x - x)) + (fabs(init_y - y)))


spiral = prepare_spiral(_input)
print(spiral)
