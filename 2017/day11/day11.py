with open('input') as f:
    _input = f.read().split(',')

direction = {'n': (0, 1), 's': (0, -1), 'ne': (1, 0), 'se': (1, -1), 'sw': (-1, 0), 'nw': (-1, 1)}
high = 0
x, y = 0, 0
for move in _input:
    tmp_x, tmp_y = direction[move]
    x, y = x + tmp_x, y + tmp_y

    if high < (abs(x) + abs(y)):
        high = (abs(x) + abs(y))

#part 1
print(x + y)

#part 2
print(high)
