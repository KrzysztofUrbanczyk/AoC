with open('input') as f:
    _input = f.readline()

steps = int(_input)
array = [0]
index = 0

for cnt in range(1, 2018):
    if len(array) > steps:
        index += steps
        if index >= len(array):
            index = index - len(array)
    else:
        for _ in range(steps):
            index += 1
            if len(array) <= index:
                index = 0

    array.insert(index + 1, cnt)
    index = index + 1

print(array[index + 1])

#part 2
array = [0]
index = 0

for cnt in range(1, 5000001):
    if len(array) > steps:
        index += steps
        if index >= len(array):
            index = index - len(array)
    else:
        for _ in range(steps):
            index += 1
            if len(array) <= index:
                index = 0

    array.insert(index + 1, cnt)
    index = index + 1

print(array[0])
print(array[1])
