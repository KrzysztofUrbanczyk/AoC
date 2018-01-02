from collections import deque

with open('input') as f:
    _input = f.readline()

steps = int(_input)
array = deque([0])

for cnt in range(1, 2018):
    array.rotate(-steps)
    array.append(cnt)

print(array[0])

#part 2
array = deque([0])

for cnt in range(1, 50000001):
    array.rotate(-steps)
    array.append(cnt)

array.rotate(-array.index(0))
print(array[1])
