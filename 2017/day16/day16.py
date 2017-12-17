with open('input') as f:
    _input = f.read()

moves = _input.split(',')
programs = 'abcdefghijklmnop'


def spin(num):
    return programs[-num:] + programs[:-num]


def exchange(x, y):
    tmp = list(programs)
    tmp[y], tmp[x] = tmp[x], tmp[y]
    return ''.join(tmp)


def partner(x, y):
    tmp = list(programs)
    z = tmp.index(x)
    w = tmp.index(y)
    tmp[z], tmp[w] = tmp[w], tmp[z]
    return ''.join(tmp)


def dance(repeat):
    global programs
    for z in range(repeat):
        for move in moves:
            if move[0] == 's':
                programs = spin(int(move[1:]))
            elif move[0] == 'x':
                args = move[1:].split('/')
                programs = exchange(int(args[0]), int(args[1]))
            elif move[0] == 'p':
                args = move[1:].split('/')
                programs = partner(args[0], args[1])
    return programs


print(dance(1))
#dance(1000000000)



