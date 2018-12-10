import re

import numpy as np

with open('input') as f:
    _input = f.read().splitlines()

pattern = re.compile("^position=<(?P<x>.*?),(?P<y>.*?)>\svelocity=<(?P<vx>.*?),(?P<vy>.*?)>$")


class Point:
    X = int
    Y = int
    VX = int
    VY = int

    def __init__(self, x, y, vx, vy):
        self.X = x
        self.Y = y
        self.VX = vx
        self.VY = vy


coordinates = list()
for line in _input:
    match = pattern.match(line)
    x = int(match.group("x"))
    y = int(match.group("y"))
    vx = int(match.group("vx"))
    vy = int(match.group("vy"))
    coordinates.append(Point(x, y, vx, vy))


prev_size = 999999999
for i in range(999999999):
    for point in coordinates:
        point.X += point.VX
        point.Y += point.VY

    X = list(map(lambda x: x.Y, coordinates))
    Y = list(map(lambda x: x.X, coordinates))

    array_size = max(X + Y) + 1
    if array_size > prev_size:
        for point in coordinates:
            point.X -= point.VX
            point.Y -= point.VY

        X = list(map(lambda x: x.Y, coordinates))
        Y = list(map(lambda x: x.X, coordinates))

        matrix = np.chararray([array_size, array_size], unicode=True)
        matrix[:] = '.'
        matrix[X, Y] = '#'

        print('\n'.join(''.join(str(cell) for cell in row) for row in matrix))
        print(i)
        break

    prev_size = array_size
