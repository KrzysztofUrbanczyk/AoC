with open('input') as f:
    _input = f.read().splitlines()

result = 0
for line in _input:
    numbers = list(map(int, line.split('\t')))
    for dividend in numbers:
        for divisor in numbers:
            if (dividend % divisor) == 0 and (dividend / divisor) > 1:
                result += dividend / divisor

print(result)
