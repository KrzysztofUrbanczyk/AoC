_input = open("input", "r").read()

#part 1
result = 0
if _input[0] == _input[-1]:
        result += int(_input[0])

for x in range(len(_input) - 1):
    if _input[x] == _input[x + 1]:
        result += int(_input[x])

print(result)

#part 2
result = 0
half = len(_input) // 2

for x in range(len(_input) - half):
    if _input[x] == _input[x + half]:
        result += int(_input[x])

for x in range(len(_input) - half, len(_input)):
    if _input[x] == _input[x - half]:
        result += int(_input[x])

print(result)