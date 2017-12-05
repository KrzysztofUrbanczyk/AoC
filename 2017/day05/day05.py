with open('input') as f:
    _input = f.read().splitlines()

numbers = list(map(lambda x: int(x), _input))
size = len(numbers)

#part 1
index = 0
counter = 0

while True:
    new_index = numbers[index]
    numbers[index] += 1
    index += new_index
    counter += 1

    if size <= index:
        break

print(counter)

#part 2

numbers = list(map(lambda x: int(x), _input))
index = 0
counter = 0
while True:
    new_index = numbers[index]
    if numbers[index] > 2:
        numbers[index] -= 1
    else:
        numbers[index] += 1

    index += new_index
    counter += 1
    if size <= index:
        break

print(counter)
