_input = 368078

NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)  # directions
turn_right = {NORTH: E, E: S, S: W, W: NORTH}  # old -> new direction
around = (0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)


def values_around(matrix, y, x):
    result = 0
    for pos in around:
        if matrix[y + pos[0]][x + pos[1]] is not None:
            result += matrix[y + pos[0]][x + pos[1]]
    return result


def spiral(width, height):
    x, y = width // 2, height // 2
    dx, dy = W
    matrix = [[None] * (width + 1) for _ in range(height + 1)]
    count = 0
    while True:
        count += 1
        if count == 1:
            matrix[y][x] = count
        else:
            result = values_around(matrix, y, x)
            matrix[y][x] = result
            if result > _input:
                return result
        new_dx, new_dy = turn_right[dx, dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
                matrix[new_y][new_x] is None):
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else:
            x, y = x + dx, y + dy


print(spiral(100, 100))

