import  re
from collections import deque

with open('input') as f:
    _input = f.read()


def play(players, last_marble):
    array = deque([0])
    scores = [0 for _ in range(players)]

    for cnt in range(1, last_marble + 1):
        if cnt % 23 == 0:
            array.rotate(7)
            scores[cnt % players] += (cnt + array.pop())
            array.rotate(-1)
        else:
            array.rotate(-1)
            array.append(cnt)

    return max(scores)


pattern = re.compile("^(?P<players>.*?) players; last marble is worth (?P<last_marble>.*?) points$")
match = pattern.match(_input)
players = int(match.group("players"))
last_marble = int(match.group("last_marble"))

print(play(players, last_marble))
print(play(players, last_marble * 100))
