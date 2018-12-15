import numpy as np

with open('input') as f:
    _input = list(map(lambda line: list(line), f.read().splitlines()))


class Cart:
    X = int
    Y = int
    Turns = int
    Direction = str

    def __init__(self, x, y, direction):
        self.X = x
        self.Y = y
        self.Turns = -1
        self.Direction = direction

    def move(self):
        tmp_x, tmp_y = forward[self.Direction]
        self.X += tmp_x
        self.Y += tmp_y

    def set_direction(self, field):
        if field == "+":
            self.turn()
        elif field == "/":
            self.Direction = curve_slash[self.Direction]
        elif field == "\\":
            self.Direction = curve_backslash[self.Direction]

    def turn(self):
        self.Turns += 1
        action = cross_turn_order[self.Turns % 3]
        self.Direction = action(self.Direction)


carts_map = np.array(_input)

N, S, W, E = (-1, 0), (1, 0), (0, -1), (0, 1)
forward = {"^": N, "<": W, ">": E, "v": S}
turn_left = {"^": "<", "<": "v", ">": "^", "v": ">"}
turn_right = {"^": ">", "<": "^", ">": "v", "v": "<"}
curve_slash = {"^": ">", "<": "v", ">": "^", "v": "<"}
curve_backslash = {"^": "<", "<": "^", ">": "v", "v": ">"}
cart_types = ["^", ">", "<", "v"]


def L(current_direction):
    return turn_left[current_direction]


def F(current_direction):
    return current_direction


def R(current_direction):
    return turn_right[current_direction]


cross_turn_order = [L, F, R]
carts = list()

for i in range(len(carts_map)):
    for j in range(len(carts_map[i])):
        if carts_map[i][j] in cart_types:
            carts.append(Cart(i, j, carts_map[i][j]))
            if carts_map[i][j] == "<" or carts_map[i][j] == ">":
                carts_map[i][j] = "-"
            else:
                carts_map[i][j] = "|"


first_crash = True
while True:
    crashes = list()
    carts.sort(key=lambda x: (x.X, x.Y))
    for cart in carts:
        cart.move()
        cart.set_direction(carts_map[cart.X][cart.Y])

        coords = list(map(lambda x: [x.X, x.Y], carts))

        if any(coords.count(x) > 1 for x in coords):
            crashes = [x for n, x in enumerate(coords) if x in coords[:n]][0]
            carts = [x for x in carts if x.X != crashes[0] and x.Y != crashes[1]]
            if first_crash:
                print(crashes)
                first_crash = False

    if len(carts) == 1:
        print(list(map(lambda x: [x.X, x.Y], carts))[0])
        break



