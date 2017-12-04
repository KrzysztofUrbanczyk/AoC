from itertools import combinations
from collections import Counter


def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)


with open('input') as f:
    _input = f.read().splitlines()

result = 0

for line in _input:
    is_valid = True
    words = line.split(" ")
    for x, y in combinations(words, 2):
        if x == y or is_anagram(x, y):
            is_valid = False

    if is_valid:
        result += 1

print(result)
