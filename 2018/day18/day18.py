from copy import deepcopy

with open('input') as f:
    _input = list(map(lambda x: list(x), f.read().splitlines()))


def op(elements):
    if elements["|"] >= 3:
        return "|"
    else:
        return "."


def tr(elements):
    if elements["#"] >= 3:
        return "#"
    else:
        return "|"


def lu(elements):
    if elements["#"] >= 1 and elements["|"] >= 1:
        return "#"
    else:
        return "."


actions = {".": op, "|": tr, "#": lu}
around = (0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)
size = 50


def calculate_resource(minutes):
    lumber_area = deepcopy(_input)
    seen = list()
    first = 0
    second = False
    countdown = False
    count = 1

    for i in range(minutes):
        new_lumber_area = deepcopy(lumber_area)
        for x in range(size):
            for y in range(size):
                elements_around = {".": 0, "|": 0, "#": 0}
                for a in around:
                    x2, y2 = a
                    if x + x2 < 0 or x + x2 > size - 1 or y + y2 < 0 or y + y2 > size - 1:
                        continue
                    elements_around[lumber_area[x + x2][y + y2]] += 1

                action = actions[lumber_area[x][y]]
                new_lumber_area[x][y] = action(elements_around)
        lumber_area = new_lumber_area

        if new_lumber_area in seen:
            seen = list()
            seen.append(new_lumber_area)
            if second:
                count = (minutes - first) % (i - first)
                countdown = True

            first = i
            second = True
        else:
            seen.append(new_lumber_area)

        if countdown:
            count -= 1

        if count == 0:
            break

    wood = 0
    lumberyards = 0
    for x in range(size):
        for y in range(size):
            if lumber_area[x][y] == "|":
                wood += 1
            if lumber_area[x][y] == "#":
                lumberyards += 1

    print(wood * lumberyards)


calculate_resource(10)
calculate_resource(1000000000)
