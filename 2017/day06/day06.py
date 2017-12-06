with open("input") as f:
    _input = f.read().split('\t')

memory_banks = list(map(lambda x: int(x), _input))
memory_size = len(memory_banks)
result = 0

history = list()
history.append(" ".join(map(str, memory_banks)))

while True:
    result += 1
    max_value = max(memory_banks)
    index = memory_banks.index(max_value)
    memory_banks[index] = 0

    for i in range(max_value):
        index += 1
        if index == memory_size:
            index = 0

        memory_banks[index] += 1

    tmp_history = " ".join(map(str, memory_banks))

    if tmp_history in history:
        search_value = tmp_history
        break

    history.append(tmp_history)

#part 1
print(result)

#part 2
print(len(history) - history.index(search_value))
