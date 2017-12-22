import re
import numpy as np

with open('input') as f:
    _input = f.read().splitlines()

buffer = list()

for line in _input:
    buffer.append(np.split(np.array([int(s) for s in re.findall(r'-\d+|\d+', line)]), 3))

closest = 99999999999
result = 0

buffer_checker = dict()
for z in range(len(_input)):
    buffer_checker[z] = True

for i in range(4500):
    values = list()
    for index, part in enumerate(buffer):
        part[1][0] += part[2][0]
        part[1][1] += part[2][1]
        part[1][2] += part[2][2]

        part[0][0] += part[1][0]
        part[0][1] += part[1][1]
        part[0][2] += part[1][2]

        if buffer_checker[index]:
            values.append(str(part[0]))

        loc = (abs(part[0][0]) + abs(part[0][1]) + abs(part[0][2]))

        if loc < closest and i > 4000:
            closest = loc
            result = index

    duplicates = set([x for x in values if values.count(x) > 1])
    if len(duplicates) != 0:
        for index, part in enumerate(buffer):
            if str(part[0]) in duplicates:
                buffer_checker[index] = False

#part 1
print(result)

#part 2
print(sum(x for x in buffer_checker.values()))


