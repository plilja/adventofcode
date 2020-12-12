import sys
import copy

DELTAS = [(1, 0),
          (1, 1),
          (0, 1),
          (-1, 1),
          (-1, 0),
          (-1, -1),
          (0, -1),
          (1, -1)]

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'


def safe_get(seats, x, y):
    if y < 0 or y >= len(seats):
        return FLOOR
    if x < 0 or x >= len(seats[y]):
        return FLOOR
    return seats[y][x]


def step1(inp):
    seats = [copy.deepcopy(inp), copy.deepcopy(inp)]
    i = 0
    while True:
        changes = 0
        for y in range(0, len(seats[i % 2])):
            for x in range(0, len(seats[i % 2][y])):
                seat = seats[i % 2][y][x]
                in_proximity = 0
                for dx, dy in DELTAS:
                    if safe_get(seats[i % 2], x + dx, y + dy) == OCCUPIED:
                        in_proximity += 1

                if seat == EMPTY and in_proximity == 0:
                    seats[(i + 1) % 2][y][x] = OCCUPIED
                    changes += 1
                elif seat == OCCUPIED and in_proximity >= 4:
                    seats[(i + 1) % 2][y][x] = EMPTY
                    changes += 1
                else:
                    seats[(i + 1) % 2][y][x] = seat
        if changes == 0:
            break
        i += 1

    result = 0
    for y in range(0, len(seats[i % 2])):
        for x in range(0, len(seats[i % 2][y])):
            if seats[i % 2][y][x] == OCCUPIED:
                result += 1
    return result


inp = [list(x.strip()) for x in sys.stdin]
print(step1(inp))
