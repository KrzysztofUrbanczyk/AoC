_input = 368078

NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)
turn_right = {NORTH: E, E: S, S: W, W: NORTH}


def spiral(width, height):
    x, y = width // 2, height // 2
    dx, dy = NORTH
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count
        new_dx, new_dy = turn_right[dx, dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
                matrix[new_y][new_x] is None):
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else:  # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix


array = spiral(607, 607)

for x in range(607):
    for y in range(607):
        if array[y][x] == _input:
            print((303 - x) + (303 - y))


