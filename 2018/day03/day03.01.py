import re

with open('input') as f:
    _input = f.read().splitlines()

array_size = 2000
array = [[0] * array_size for _ in range(array_size)]
pattern = re.compile("^.(?P<id>.*?)\s@\s(?P<x>.*?),(?P<y>.*?):\s(?P<a>.*?)x(?P<b>.*?)$")


for line in _input:
    match = pattern.match(line)

    x = int(match.group("x"))
    y = int(match.group("y"))
    a = int(match.group("a"))
    b = int(match.group("b"))

    for i in range(a):
        for j in range(b):
            new_x, new_y = x + i, y + j
            array[new_x][new_y] += 1

result = 0
for i in range(array_size):
    for j in range(array_size):
        if array[i][j] > 1:
            result += 1

print(result)



