with open('input') as f:
    _input = f.readlines()

gen_a_factor = 16807
gen_b_factor = 48271
divisor = 2147483647


#part 1
gen_a = int(_input[0])
gen_b = int(_input[1])
result = 0

for i in range(40000000):
    gen_a = (gen_a * gen_a_factor) % divisor
    gen_b = (gen_b * gen_b_factor) % divisor

    binary_a = "{0:b}".format(gen_a).zfill(32)
    binary_b = "{0:b}".format(gen_b).zfill(32)

    if binary_a[16:] == binary_b[16:]:
        result += 1

print(result)


#part 2
def get_gen_value(prev_value, factor, divisor_condition):
    gen_result = prev_value
    while True:
        gen_result = (gen_result * factor) % divisor
        if gen_result % divisor_condition == 0:
            return gen_result


gen_a = int(_input[0])
gen_b = int(_input[1])
result = 0

for _ in range(5000000):
    gen_a = get_gen_value(gen_a, gen_a_factor, 4)
    gen_b = get_gen_value(gen_b, gen_b_factor, 8)

    binary_a = "{0:b}".format(gen_a).zfill(32)
    binary_b = "{0:b}".format(gen_b).zfill(32)

    if binary_a[16:] == binary_b[16:]:
        result += 1

print(result)
