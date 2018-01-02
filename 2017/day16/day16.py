with open('input') as f:
    _input = f.read()

moves = _input.split(',')
start_programs = 'abcdefghijklmnop'


def spin(num, programs):
    return programs[-num:] + programs[:-num]


def exchange(x, y, programs):
    tmp = list(programs)
    tmp[y], tmp[x] = tmp[x], tmp[y]
    return ''.join(tmp)


def partner(x, y, programs):
    tmp = list(programs)
    z = tmp.index(x)
    w = tmp.index(y)
    tmp[z], tmp[w] = tmp[w], tmp[z]
    return ''.join(tmp)


def dance(repeat, programs):
    seen = []
    for i in range(repeat):
        if programs in seen:
            print(seen[repeat % i])
            return
        seen.append(programs)
        for move in moves:
            if move[0] == 's':
                programs = spin(int(move[1:]), programs)
            elif move[0] == 'x':
                args = move[1:].split('/')
                programs = exchange(int(args[0]), int(args[1]), programs)
            elif move[0] == 'p':
                args = move[1:].split('/')
                programs = partner(args[0], args[1], programs)
    print(programs)


#part 1
dance(1, start_programs)

#part 2
dance(1000000000, start_programs)



