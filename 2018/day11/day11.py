with open('input') as f:
    _input = int(f.read())

array_size = 300


def get_power_level(x, y):
    rack_id = x + 10
    power_level = (((rack_id * y) + _input) * rack_id)
    if power_level < 99:
        return 0
    else:
        return int(str(power_level)[-3:][0]) - 5


def find_max_area(scan_size):
    array = [[get_power_level(x, y) for x in range(array_size)] for y in range(array_size)]

    x, y = 0, 0
    for scan_size in range(1, scan_size + 1):
        max_power_level_area = 0
        for i in range(array_size - scan_size):
            for j in range(array_size - scan_size):
                result = 0
                for si in range(scan_size):
                    for sj in range(scan_size):
                        result += array[i + si][j + sj]

                if result > max_power_level_area:
                    max_power_level_area = result
                    x, y = i, j
        print(x, y, scan_size, max_power_level_area)


find_max_area(3)
find_max_area(300)
