with open('input') as f:
    _input = f.read().splitlines()

result = 0

for line in _input:
    words = line.split(" ")
    if  len(set(words)) == len(words):
        result += 1

print(result)
