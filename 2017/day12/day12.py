with open('input') as f:
    _input = f.read().splitlines()


def get_programs(input_lines, programs, name):
    line_elements = [x for x in _input if x.startswith(name)][0].split(' <-> ')
    programs.add(line_elements[0])

    for program in map(str.strip, line_elements[1].split(',')):
        if program in programs:
            continue
        else:
            get_programs(input_lines, programs, program)


#part 1
programs = set()
get_programs(_input, programs, '0')

print(len(programs))

#part 2
groups = 1

for line in _input:
    program = line.split(' <-> ')[0]
    if program not in programs:
        get_programs(_input, programs, program)
        groups += 1

print(groups)
