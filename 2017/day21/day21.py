import numpy as np

with open('input') as f:
    _input = f.read().splitlines()


def get_rule(array):
    return '/'.join(map(lambda x: ''.join(x), array))


def find_rule(rule):
    return [x for x in _input if x.startswith(rule)]


def get_rules(array):
    rules = flip(array)
    for _ in range(3):
        array = np.rot90(array)
        rules += flip(array)
    return set(rules)


def flip(array):
    return [get_rule(array),
            get_rule(np.flip(array, 1)),
            get_rule(np.flip(array, 0)),
            get_rule(np.flip(np.flip(array, 1), 0))]


def blockshaped(arr, nrows, ncols):
    h, w = arr.shape
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))


def find_new_array(array):
    for rule in get_rules(array):
        new_rule = [x for x in _input if x.startswith(rule)]
        if new_rule:
            n = new_rule[0].split(' => ')[1]
            return list(map(lambda x: list(x), n.split('/')))


start = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]

second = False
for _ in range(12):
    size = len(start[0])
    if size % 3 == 0:
        zz = []
        arrays = blockshaped(np.array(start), 3, 3)
        for ar in arrays:
            cc = np.array(find_new_array(ar.tolist())).reshape(4, 4)
            if len(zz) > 0:
                zz = np.concatenate((zz, cc.T), axis=1)
            else:
                zz = cc
        start = zz
        if second:
            dd = np.hsplit(start, 2)
            for i in range(len(dd)):
                start = np.vstack((dd))
        second = True
    elif size % 2 == 0:
        zz = []
        arrays = blockshaped(np.array(start), 2, 2)
        for ar in arrays:
            cc = np.array(find_new_array(ar.tolist())).reshape(3,3)
            if len(zz) > 0:
                zz = np.concatenate((zz, cc.T), axis=1)
            else:
                zz = cc
        start = zz
        dd = np.hsplit(start, 2)
        start = np.vstack((dd[0], dd[1]))


xx = start.tolist()
result = 0
for l in xx:
    for c in l:
        if c == '#':
            result += 1
print(result)
