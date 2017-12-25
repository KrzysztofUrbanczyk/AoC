with open('input') as f:
    _input = f.read().splitlines()

state = _input[0][-2]
iteration = int(_input[1].split(" ")[-2])

array = [0] * iteration
index = iteration // 2


def move(i, direction):
    if direction == 'right.':
        i += 1
    else:
        i -= 1
    return i


for z in range(iteration):
    in_state = f'In state {state}:'
    blueprint_index = _input.index(in_state)
    if array[index] == 0:
        blueprint_index += 2
        array[index] = int(_input[blueprint_index][-2])

    else:
        blueprint_index += 6
        array[index] = int(_input[blueprint_index][-2])

    blueprint_index += 1
    index = move(index, _input[blueprint_index].split(" ")[-1])
    state = _input[blueprint_index + 1][-2]


print(sum(array))

