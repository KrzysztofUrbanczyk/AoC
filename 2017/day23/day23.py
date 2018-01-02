with open('input') as f:
    _input = f.read().splitlines()

registers = dict.fromkeys('abcdefgh', 0)
index = 0


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def set(x, y):
    if is_digit(y):
        registers[x] = int(y)
    else:
        registers[x] = registers[y]


def sub(x, y):
    if is_digit(y):
        registers[x] -= int(y)
    else:
        registers[x] -= registers[y]


def mul(x, y):
    if is_digit(y):
        registers[x] *= int(y)
    else:
        registers[x] *= registers[y]


def jnz(x, y, index):
    if is_digit(x) and x != 0:
        index += int(y)
    elif registers[x] != 0:
        index += int(y)
    else:
        index += 1
    return index


operations = {'set': set, 'sub': sub, 'mul': mul}
result = 0
while True:
    if index >= len(_input):
        break
    func, x, y = _input[index].split(' ')
    if func == 'jnz':
        index = jnz(x, y, index)
        continue
    else:
        if func == 'mul':
            result += 1
        operations[func](x, y)
        index += 1

print(result)
