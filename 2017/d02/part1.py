with open('input') as f:
    _input = f.read().splitlines()

result = 0
for line in _input:
    numbers = list(map(int, line.split('\t')))
    result += int(max(numbers)) - int(min(numbers))

print(result)



