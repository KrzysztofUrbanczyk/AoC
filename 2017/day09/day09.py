with open('input') as f:
    _input = f.read()

bracer_counter = 0
is_garbage_open = False

groups_score = 0
index = 0

garbage = 0


while True:
    if _input[index] == '!':
        index += 2
        continue

    if _input[index] == '<':
        if not is_garbage_open:
            garbage -= 1
        is_garbage_open = True

    if is_garbage_open and _input[index] != '>':
        index += 1
        garbage += 1
        continue

    if _input[index] == '>':
        is_garbage_open = False

    if _input[index] == '{':
        bracer_counter += 1
        groups_score += bracer_counter

    if _input[index] == '}':
        bracer_counter -= 1

    if len(_input) - 1 == index:
        break
    else:
        index += 1

#part 1
print(groups_score)

#part 2
print(garbage)
