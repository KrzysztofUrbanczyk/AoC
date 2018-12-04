import re

with open('input') as f:
    _input = f.read().splitlines()


def init_minutes():
    result = {}
    for x in range(60):
        result[x] = 0
    return result


_input.sort()
guards = {}
guard_id = ""


for i, line in enumerate(_input):
    if "wake" in line:
        continue

    if "Guard" in line:
        guard_id = int(re.search('.*#(\d*)\s.*', line).group(1))
        if guard_id not in guards:
            guards[guard_id] = init_minutes()
    else:
        sleep_start = int(re.search(".*:(\d*)\].*", line).group(1))
        sleep_stop = int(re.search(".*:(.\d*)\].*", _input[i + 1]).group(1))

        for j in range(sleep_start, sleep_stop):
            guards[guard_id][j] += 1


part1 = {}
for key in guards:
    part1[key] = sum(guards[key].values())

guard_with_most_minute_asleep = max(part1, key=lambda x: part1[x])
most_asleep_minute = max(guards[guard_with_most_minute_asleep], key=lambda x: guards[guard_with_most_minute_asleep][x])
print(guard_with_most_minute_asleep * most_asleep_minute)


part2 = {}
for key in guards:
    part2[key] = max(guards[key], key=lambda x: guards[key][x])


guard_which_most_frequently_asleep = max(part2, key=lambda x: part2[x])
print(part2[guard_which_most_frequently_asleep] * guard_which_most_frequently_asleep)

