with open('input') as f:
    _input = f.read().splitlines()


class Point:
    X = int
    Y = int

    def __init__(self, x, y):
        self.X = x
        self.Y = y


coordinates = dict()
max_coordinate = 0

for z in range(len(_input)):
    x, y = _input[z].split(", ")
    coordinates[z + 1] = Point(int(x), int(y))
    max_coordinate = max(int(x), int(y), max_coordinate)

max_coordinate += 2
array = [[0] * max_coordinate for _ in range(max_coordinate)]

for i in range(max_coordinate):
    for j in range(max_coordinate):
        distances = dict()
        for key in coordinates:
            distances[key] = abs(i - coordinates[key].X) + abs(j - coordinates[key].Y)

        min_distance = min(distances.values())
        same_min = 0
        for z in distances:
            if distances[z] == min_distance:
                same_min += 1

        if same_min == 1:
            array[i][j] = min(distances, key=lambda x: distances[x])

excluded = set()
for i in range(max_coordinate):
    excluded.add(array[i][0])
    excluded.add(array[0][i])
    excluded.add(array[i][max_coordinate - 1])
    excluded.add(array[max_coordinate - 1][i])


result = dict()
for i in range(max_coordinate):
    for j in range(max_coordinate):
        location = array[i][j]
        if location not in excluded:
            if location not in result.keys():
                result[location] = 0
            result[location] += 1

print(max(result.values()))


max_value = 10000
array = [[0] * max_coordinate for _ in range(max_coordinate)]
result = 0
for i in range(max_coordinate):
    for j in range(max_coordinate):
        distances = list()
        for key in coordinates:
            distances.append(abs(i - coordinates[key].X) + abs(j - coordinates[key].Y))

        if sum(distances) < max_value:
            result += 1

print(result)
