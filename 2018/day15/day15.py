import collections

with open('input') as f:
    _input = list(map(lambda x: list(x), f.read().splitlines()))

N, S, W, E = (-1, 0), (1, 0), (0, -1), (0, 1)
action_order = [N, W, E, S]
wall, clear = "#", "."


class Unit:
    Race = str
    Atk = int
    HP = int
    X = int
    Y = int

    def __init__(self, race, x, y):
        self.Atk = 3
        self.HP = 200
        self.Race = race
        self.X = x
        self.Y = y

    def is_enemy_near(self):
        result = False
        for direction in action_order:
            x, y = direction
            if area[self.X + x][self.Y + y] == self.get_opposite_race():
                result = True
        return result

    def attack(self):
        x, y = self.X, self.Y
        enemy_around = list()
        for x2, y2 in ((x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)):
            if area[x2][y2] == self.get_opposite_race():
                for enemy in filter(lambda x: x.X == x2 and x.Y == y2 , units):
                    enemy_around.append(enemy)

        if len(enemy_around) > 0:
            min_hp = min(enemy_around, key=lambda x: x.HP).HP
            for x2, y2 in ((x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)):
                enemy = list(filter(lambda x: x.X == x2 and x.Y == y2 and x.HP == min_hp, units))
                if len(enemy) > 0:
                    enemy[0].HP -= 3
                    if enemy[0].HP <= 0:
                        area[enemy[0].X][enemy[0].Y] = clear
                        units.remove(enemy[0])
                    break

    def move(self):
        squares = list()
        for enemy in filter(lambda x: x.Race == self.get_opposite_race(), units):
            for x, y in ((enemy.X - 1, enemy.Y), (enemy.X, enemy.Y - 1), (enemy.X, enemy.Y + 1), (enemy.X + 1, enemy.Y)):
                if area[x][y] == clear:
                    squares.append([x, y])

        path = self.get_path_to_nearest_enemy(squares)

        if path is not None and len(path) > 0:
            self.X, self.Y = path[1]

    def get_path_to_nearest_enemy(self, goal):
        start = (self.X, self.Y)
        queue = collections.deque([[start]])
        seen = {start}
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if [x, y] in goal:
                return path

            for x2, y2 in ((x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)):
                if area[x2][y2] != wall and area[x2][y2] == clear and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))

    def get_opposite_race(self):
        if self.Race == "G":
            return "E"
        else:
            return "G"


def update_area():
    for i in range(len(area)):
        for j in range(len(area)):
            if area[i][j] == "E" or area[i][j] == "G":
                area[i][j] = clear
    for unit in units:
        area[unit.X][unit.Y] = unit.Race


units = list()
area = _input

'''
for line in area:
    print("".join(line))
'''
for i in range(len(area)):
    for j in range(len(area)):
        if area[i][j] == "E" or area[i][j] == "G":
            units.append(Unit(area[i][j], i, j))


for i in range(0, 100):
    units.sort(key=lambda unit: (unit.X, unit.Y))

    for unit in units:
        if unit.is_enemy_near():
            unit.attack()
        else:
            unit.move()
            if unit.is_enemy_near():
                unit.attack()
        update_area()


    units.sort(key=lambda unit: (unit.X, unit.Y))

    print(i)
    for line in area:
        print("".join(line))

    goblis = list(filter(lambda x: x.Race == "G" ,units))
    elfs = list(filter(lambda x: x.Race == "E", units))

    if len(goblis) == 0 or len(elfs) == 0:
        result = 0
        for u in units:
            print(u.HP)
            result += u.HP
        print(result * i)
        break
