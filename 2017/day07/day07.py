with open('input') as f:
    _input = f.read().splitlines()

#part 1
programs = set()
root_name = ""

for line in _input:
    if '>' in line:
        programs |= set(map(str.strip, line.split('>')[1].split(',')))

for line in _input:
    root_name = line.split(' ')[0]
    if root_name not in programs:
        break

print(root_name)


#part 2
def get_programs_weight(program_name, all_programs):
    weight_sum = 0
    program = ''
    for item in all_programs:
        if item.startswith(program_name):
            program = item
            break

    if '>' in program:
        sub_programs = map(str.strip, program.split('>')[1].split(','))
        for sub_p in sub_programs:
            weight_sum += get_programs_weight(sub_p, _input)
    weight_sum += int(program[program.find("(") + 1:program.find(")")])
    return weight_sum


for line in _input:
    if line.startswith(root_name):
        root = line

sub_programs = list(map(str.strip, root.split('>')[1].split(',')))
result = []
for i in range(5):
    result.append(get_programs_weight(sub_programs[i], _input))

print(result)

#TODO dorobienie wyszukiwania
