_input = open("input1", "r").read()

result = 0
if _input[0] == _input[-1]:
        result += int(_input[0])

for x in range(len(_input) - 1):
    if _input[x] == _input[x + 1]:
        result += int(_input[x])

print(result)
