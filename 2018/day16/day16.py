import re
with open('input') as f:
    _input = f.read().splitlines()

with open('input2') as f:
    _input2 = f.read().splitlines()


def addr(a, b, c):
    registers[c] = registers[a] + registers[b]


def addi(a, b, c):
    registers[c] = registers[a] + b


def mulr(a, b, c):
    registers[c] = registers[a] * registers[b]


def muli(a, b, c):
    registers[c] = registers[a] * b


def banr(a, b, c):
    registers[c] = registers[a] & registers[b]


def bani(a, b, c):
    registers[c] = registers[a] & b


def borr(a, b, c):
    registers[c] = registers[a] | registers[b]


def bori(a, b, c):
    registers[c] = registers[a] | b


def setr(a, b, c):
    registers[c] = registers[a]


def seti(a, b, c):
    registers[c] = a


def gtir(a, b, c):
    if a > registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0


def gtri(a, b, c):
    if registers[a] > b:
        registers[c] = 1
    else:
        registers[c] = 0


def gtrr(a, b, c):
    if registers[a] > registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0


def eqir(a, b, c):
    if a == registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0


def eqri(a, b, c):
    if registers[a] == b:
        registers[c] = 1
    else:
        registers[c] = 0


def eqrr(a, b, c):
    if registers[a] == registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0


registers = [0, 0, 0, 0]
instructions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
occurrences = {}

result = 0
i = 0
while i < len(_input):
    before = list(map(int, re.search(".*\[(.*)\].*", _input[i]).group(1).split(", ")))
    action = list(map(int, _input[i + 1].split(" ")))
    after = list(map(int, re.search(".*\[(.*)\].*", _input[i + 2]).group(1).split(", ")))
    like = 0
    for ins in instructions:
        registers = before.copy()
        ins(action[1], action[2], action[3])
        if registers == after:
            like += 1
            if action[0] not in occurrences:
                occurrences[action[0]] = [ins.__name__]
            else:
                occurrences[action[0]].append(ins.__name__)

    if like >= 3:
        result += 1
    i += 4

print(result)


for key in occurrences:
    occurrences[key] = set(occurrences[key])

bind = dict()
seen = set()

for i in range(16):
    for key in occurrences:
        for se in seen:
            if se in occurrences[key]:
                occurrences[key].remove(se)
        if len(occurrences[key]) == 1:
            bind[key] = list(occurrences[key])[0]
            seen.add(list(occurrences[key])[0])

    for se in seen:
        occurrences.pop(se, None)

registers = [0, 0, 0, 0]

for line in _input2:
    values = list(map(int, line.split(" ")))
    action = list(filter(lambda x: x.__name__ == bind[values[0]], instructions))[0]
    action(values[1], values[2], values[3])

print(registers[0])