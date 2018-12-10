import re

with open('input') as f:
    _input = f.read().splitlines()

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


first_steps = list()
for key in forward.keys():
    if key not in backward:
        first_steps.append(key)

first_steps.sort()

for node in nodes:
    if node not in backward:
        backward[node] = ""

result = ""


def process_steps(parent, left):
    global result
    result += parent
    if len(result) == len(nodes):
        return result
    left.remove(parent)
    left += forward[parent]
    left = list(set(left))
    left.sort()

    for step in left:
        if all(item in result for item in backward[step]):
            return process_steps(step, left)


print(process_steps(first_steps[0], first_steps))
