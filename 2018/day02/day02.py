import difflib
from collections import Counter
from itertools import combinations

with open('input') as f:
    _input = f.read().splitlines()

two = 0
three = 0

#part 1
for line in _input:
    letterCount = Counter(line).values()
    if 2 in letterCount:
        two += 1
    if 3 in letterCount:
        three += 1

print(two * three)

#part 2

result = ""

for seq1, seq2 in combinations(_input, 2):
    difference = sum(1 for a, b in zip(seq1, seq2) if a != b)
    if difference == 1:
        for i, s in enumerate(difflib.ndiff(seq1, seq2)):
            if s[0] == ' ':
                result += s[-1]

        print(result)
        break

