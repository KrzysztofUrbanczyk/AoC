with open('input') as f:
    _input = f.readlines()

#part 1
result = 0

for line in _input:
    items = line.split(': ')
    layer = int(items[0])
    layer_range = int(items[1])

    if layer % (layer_range - 1) * 2 == 0 and layer > layer_range:
        result += layer_range * layer

print(result)


# part 2
cnt = 0

while True:
    hit = False
    for line in _input:
        items = line.split(': ')
        layer = int(items[0])
        layer_range = int(items[1])
        if (layer + cnt) % ((layer_range - 1) * 2) == 0:
            hit = True
            break

    if not hit:
        print(cnt)
        break
    cnt += 1



