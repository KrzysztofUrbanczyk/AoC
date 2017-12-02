_input = open("input2", "r").read()

result = 0
half = len(_input) // 2

for x in range(len(_input) - half):
    if _input[x] == _input[x + half]:
        result += int(_input[x])

for x in range(len(_input) - half, len(_input)):
    if _input[x] == _input[x - half]:
        result += int(_input[x])

print(result)