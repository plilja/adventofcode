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


def safe_get(seats, x, dx, y, dy):
    if y < 0 or y >= len(seats):
        return FLOOR
    if x < 0 or x >= len(seats[y]):
        return FLOOR
    return seats[y][x]


def get_diagonal(seats, x, dx, y, dy):
    while y >= 0 and y < len(seats) and \
            x >= 0 and x < len(seats[0]):
        seat = seats[y][x]
        if seat != FLOOR:
            return seat
        else:
            x += dx
            y += dy
    return FLOOR


def solve(inp, nearby_seat_func, limit):
    seats = [copy.deepcopy(inp), copy.deepcopy(inp)]
    i = 0
    while True:
        changes = 0
        for y in range(0, len(seats[i % 2])):
            for x in range(0, len(seats[i % 2][y])):
                seat = seats[i % 2][y][x]
                in_proximity = 0
                for dx, dy in DELTAS:
                    if nearby_seat_func(seats[i % 2], x + dx, dx, y + dy, dy) == OCCUPIED:
                        in_proximity += 1

                if seat == EMPTY and in_proximity == 0:
                    seats[(i + 1) % 2][y][x] = OCCUPIED
                    changes += 1
                elif seat == OCCUPIED and in_proximity >= limit:
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


def step1(inp):
    return solve(inp, safe_get, 4)


def step2(inp):
    return solve(inp, get_diagonal, 5)


inp = [list(x.strip()) for x in sys.stdin]
print(step1(inp))
print(step2(inp))
