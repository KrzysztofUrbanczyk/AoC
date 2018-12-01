from itertools import cycle

with open('input') as f:
    _input = f.read().splitlines()

#part 1

result = 0
for number in _input:
    result += int(number)

print(result)


#part 2

result = 0
frequencies = set()
for number in cycle(_input):
    result += int(number)
    if result in frequencies:
        break
    frequencies.add(result)

print(result)
