with open('input') as f:
    _input = f.read().splitlines()

bridges = list()


def build_bridge(component, bridge):
    bridge += component + " "
    if len(bridge.rstrip().split('/')) == 2:
        last = component.split('/')[1]
    elif bridge.rstrip().replace("/", " ").split(" ")[-3] == component.split('/')[0] or bridge.rstrip().replace("/", " ").split(" ")[-4] == component.split('/')[0]:
        last = component.split('/')[1]
    else:
        last = component.split('/')[0]
    components = [i for i in _input if ((i.split('/')[0] == last or i.split('/')[1] == last) and i not in bridge)]
    if not components:
        return bridge
    for comp in components:
        bridges.append(build_bridge(comp, bridge))

    return bridge


zero_pin_comp = [i for i in _input if i.startswith('0')]

for component in zero_pin_comp:
    bridge = ""
    build_bridge(component, bridge)

result = list()
for bridge in bridges:
    values = list(bridge.rstrip().replace("/", " ").split(" "))
    result.append(sum(map(int, values)))

#part 1
print(max(result))


longest = list()
size = len(max(bridges, key=len))
for bridge in bridges:
    if len(bridge) == size:
        values = list(bridge.rstrip().replace("/", " ").split(" "))
        longest.append(sum(map(int, values)))

#part 2
print(max(longest))

