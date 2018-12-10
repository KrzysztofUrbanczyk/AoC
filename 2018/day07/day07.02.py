import re
from string import ascii_lowercase

with open('input') as f:
    _input = f.read().splitlines()


class Step:
    Index = str
    Time = int

    def __init__(self, index, time):
        self.Index = index
        self.Time = time


pattern = re.compile("^Step\s(?P<first>.*?)\smust be finished before step\s(?P<second>.*?)\scan begin\.$")

forward = dict()
backward = dict()
nodes = set()

for line in _input:
    match = pattern.match(line)
    first = match.group("first")
    second = match.group("second")

    nodes.add(first)
    nodes.add(second)

    if first not in forward.keys():
        forward[first] = [second]
    else:
        forward[first].append(second)

    if second not in backward.keys():
        backward[second] = [first]
    else:
        backward[second].append(first)


left = list()
for key in forward.keys():
    if key not in backward:
        left.append(key)

left.sort()

for node in nodes:
    if node not in backward:
        backward[node] = ""

result = ""

workers = dict()
workers[1] = None
workers[2] = None
workers[3] = None
workers[4] = None
workers[5] = None


LETTERS = {letter: index for index, letter in enumerate(ascii_lowercase, start=1)}

for i in range(1000):
    if len(result) == len(nodes):
        print(i)
        break
    for key in workers:
        if workers[key] is None and len(left) > 0:
            for step in left:
                if all(item in result for item in backward[step]):
                    workers[key] = Step(step, LETTERS[step.lower()] + 60)
                    left.remove(step)
                    if step in forward:
                        left += forward[step]
                        left = list(set(left))
                        left.sort()
                        break

    for key in workers:
        if workers[key] is not None:
            workers[key].Time -= 1
            if workers[key].Time == 0:
                result += workers[key].Index
                workers[key] = None


