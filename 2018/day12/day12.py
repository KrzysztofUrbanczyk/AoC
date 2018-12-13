with open('input') as f:
    _input = f.read().splitlines()

pots = _input[0].split(': ')[1]
patterns = dict()

for i in range(2, len(_input)):
    result = _input[i].split(' => ')
    patterns[result[0]] = result[1]

count = 0
for x in range(20):
    count -= 4
    pots = "...." + pots + "...."
    new_pots = ""
    for i in range(len(pots)):
        if i < 2 or i > len(pots) - 3:
            new_pots += pots[i]
        else:
            five = pots[i - 2: i + 3]
            if five in patterns.keys():
                new_pots += patterns[five]
            else:
                new_pots += "."

    cut_from = new_pots.index("#")
    cut_to = new_pots.rfind("#") + 1
    count += cut_from
    pots = new_pots[cut_from: cut_to]

result = 0
for i in pots:
    if i == "#":
        result += count
    count += 1

print(result)
