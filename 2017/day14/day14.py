with open('input') as f:
    input_puzzle = f.read()

regions_array = []

result = 0
for i in range(128):
    array = list(range(256))
    skip_size = 0
    index = 0

    _input = input_puzzle + '-' + str(i)
    _input = [ord(c) for c in _input]
    _input += 17, 31, 73, 47, 23

    for _ in range(64):
        for i in range(len(_input)):
            reverse_length = int(_input[i])
            end = index + reverse_length
            if end < len(array):
                array[index:end] = array[index:end][::-1]
            else:
                to_end = len(array) - index
                tmp_array = array[index: index + to_end] + array[0:end - len(array)]
                tmp_array = tmp_array[::-1]
                array[index:end] = tmp_array[:to_end]
                array[0:end - len(array)] = tmp_array[to_end:]

            index = (index + reverse_length + skip_size) % len(array)
            skip_size += 1

    dense_hash = [0] * 16
    i = -1
    for num in range(len(array)):
        if num % 16 == 0:
            i += 1
        dense_hash[i] ^= array[num]

    knot_hash = ''
    for ha in dense_hash:
        knot_hash += '{0:02x}'.format(ha)

    binary = bin(int(knot_hash, 16))[2:].zfill(128)
    regions_array.append(list(binary))
    result += binary.count('1')

print(result)

#part 2
directions = (1, 0), (-1, 0), (0, -1), (0, 1)


def clear_region(x, y):
    global regions_array
    regions_array[x][y] = '0'
    for direction in directions:
        tmp_x, tmp_y = x + direction[0], y + direction[1]
        if tmp_x < 0 or tmp_x > 127 or tmp_y < 0 or tmp_y > 127:
            continue
        if regions_array[tmp_x][tmp_y] == '1':
            clear_region(tmp_x, tmp_y)


regions = 0
for i in range(128):
    for j in range(128):
        if regions_array[i][j] == '1':
            regions += 1
            clear_region(i, j)

print(regions)
