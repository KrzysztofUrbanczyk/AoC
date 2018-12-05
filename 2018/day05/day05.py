import re
from string import ascii_lowercase

with open('input') as f:
    _input = f.read()


def cut_polymers(polymer):
    i = 0
    while i < len(polymer) - 1:
        x, y = polymer[i], polymer[i + 1]
        if x.casefold() == y.casefold():
            if x != y:
                polymer = polymer.replace(x + y, "")
                i = 0
        i += 1
    return polymer


#part 1
print(len(cut_polymers(_input)))

#part 2
result = list()
for c in ascii_lowercase:
    pattern = re.compile(c, re.IGNORECASE)
    result.append(len(cut_polymers(pattern.sub("", _input))))

print(min(result))
