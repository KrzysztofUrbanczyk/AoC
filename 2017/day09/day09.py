with open('input') as f:
    _input = f.read()

bracer_count = 0
garbage_open = False

result = 0
x = 0

grb = 0


while True:
    if _input[x] == '!':
        x += 2
        continue

    if _input[x] == '<':
        if not garbage_open:
            grb -= 1
        garbage_open = True

    if garbage_open and _input[x] != '>':
        x += 1
        grb += 1
        continue

    if _input[x] == '>':
        garbage_open = False

    if _input[x] == '{':
        bracer_count += 1
        result += bracer_count

    if _input[x] == '}':
        bracer_count -= 1

    if len(_input) - 1 == x:
        break
    else:
        x += 1


print(result)
print(grb)