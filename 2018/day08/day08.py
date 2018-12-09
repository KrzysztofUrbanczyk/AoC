with open('input') as f:
    _input = list(map(lambda x: int(x), f.read().split(' ')))

index = 0


def sum_metadata():
    result = 0
    global index

    childes, metadata = _input[index], _input[index + 1]
    index += 2

    while childes > 0:
        childes -= 1
        result += sum_metadata()

    while metadata > 0:
        metadata -= 1
        result += _input[index]
        index += 1

    return result


print(sum_metadata())

index = 0


def sum_metadata2():
    result = 0
    global index

    childes, metadata = _input[index], _input[index + 1]
    index += 2

    if childes != 0:
        node_values = list()

        while childes > 0:
            childes -= 1
            node_values.append(sum_metadata2())

        while metadata > 0:
            metadata -= 1
            if _input[index] <= len(node_values):
                result += node_values[_input[index] - 1]
            index += 1

    else:
        while metadata > 0:
            metadata -= 1
            result += _input[index]
            index += 1

    return result


print(sum_metadata2())
