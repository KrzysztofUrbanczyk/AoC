with open('input') as f:
    _input = f.read().splitlines()

registers_names = set()

for line in _input:
    regi = line.split(" ")[1]
    if regi.isalpha():
        registers_names.add(regi)

registers = dict.fromkeys(str.join("", registers_names), 0)
last_played_value = 0

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


def add(x, y):
    if is_digit(y):
        registers[x] += int(y)
    else:
        registers[x] += registers[y]


def mul(x, y):
    if is_digit(y):
        registers[x] *= int(y)
    else:
        registers[x] *= registers[y]


def mod(x, y):
    if is_digit(y):
        registers[x] %= int(y)
    else:
        registers[x] %= registers[y]


def rcv(x):
    if is_digit(x) and x != 0:
        print('a')
    elif registers[x] != 0:
        print('b')


def snd(x):
    if is_digit(x):
        result = int(x)
    else:
        result = registers[x]
    return result


def jgz(x, y, index):
    if is_digit(x) and int(x) > 0:
        index += int(y)
    elif registers[x] > 0:
        index += int(y)
    else:
        index += 1
    return index


unary_operations = {'snd': snd}
binary_operations = {'set': set, 'add': add, 'mul': mul, 'mod': mod}
ternary_operations = {'jgz': jgz}

index = 0
while True:
    operation = _input[index].split(' ')[0]
    if operation in ternary_operations:
        func, x, y = _input[index].split(' ')
        index = ternary_operations[func](x, y, index)
        continue
    elif operation in binary_operations:
        func, x, y = _input[index].split(' ')
        binary_operations[func](x, y)
        index += 1
    else:
        func, x = _input[index].split(' ')
        if func == 'rcv':
            break
        last_played_value = unary_operations[func](x)
        index += 1

#part 1
print(last_played_value)
