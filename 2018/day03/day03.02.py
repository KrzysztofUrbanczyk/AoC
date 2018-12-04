import re

with open('input') as f:
    _input = f.read().splitlines()

ids = set()
overlap_ids = set()
array_size = 2000
array = [[0] * array_size for _ in range(array_size)]
pattern = re.compile("^.(?P<id>.*?)\s@\s(?P<x>.*?),(?P<y>.*?):\s(?P<a>.*?)x(?P<b>.*?)$")

for line in _input:
    match = pattern.match(line)
    rectangle_id = match.group("id")
    ids.add(int(rectangle_id))

    x = int(match.group("x"))
    y = int(match.group("y"))
    a = int(match.group("a"))
    b = int(match.group("b"))

    for i in range(a):
        for j in range(b):
            new_x, new_y = x + i, y + j
            if array[new_x][new_y] != 0:
                overlap_ids.add(array[new_x][new_y])
                overlap_ids.add(int(rectangle_id))
            array[new_x][new_y] = int(rectangle_id)

print(list(filter(lambda z: z not in overlap_ids, ids))[0])



