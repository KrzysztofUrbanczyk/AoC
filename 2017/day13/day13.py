with open('input') as f:
    _input = f.readlines()

result = 0

for line in _input:
    items = line.split(': ')
    layer = int(items[0])
    layer_range = int(items[1])

    if layer / (layer_range - 1) % 2 == 0:
        result += layer_range * layer

#part 1
print(result)

#TODO part 2 - bruteforce solution work too long