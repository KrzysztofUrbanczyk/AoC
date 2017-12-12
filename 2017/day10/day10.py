with open('input') as f:
    _input = f.read()

#part 1
array = list(range(256))
index = 0
skip_size = 0

for item in _input.split(','):
    reverse_length = int(item)
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

print(array[0] * array[1])


#part 2
array = list(range(256))
skip_size = 0
index = 0

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

result = ''
for ha in dense_hash:
    result += '{0:02x}'.format(ha)

print(result)



