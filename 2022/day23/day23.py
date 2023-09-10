import sys

from collections import defaultdict

sys.path.append("../..")
from common.util import neighbors8

MOVES = [((0, -1), [(-1, -1), (0, -1), (1, -1)]),
         ((0, 1), [(-1, 1), (0, 1), (1, 1)]),
         ((-1, 0), [(-1, -1), (-1, 0), (-1, 1)]),
         ((1, 0), [(1, -1), (1, 0), (1, 1)])]


def step1(inp):
    grid = defaultdict(bool)
    elves = []
    for y, row in enumerate(inp):
        for x, v in enumerate(row):
            if v == '.':
                grid[(x, y)] = False
            else:
                assert v == '#'
                grid[(x, y)] = True
                elves.append((x, y))
    moves = MOVES[::]
    for _ in range(0, 10):
        elf_to_next_pos = {}
        pos_to_count = defaultdict(int)
        for x, y in elves:
            occupied_neighbours = sum([1 if grid[(x2, y2)] else 0 for (x2, y2) in neighbors8(x, y)])
            if occupied_neighbours == 0:
                continue
            for (dx, dy), to_check in moves:
                possible = True
                for dx2, dy2, in to_check:
                    if grid[(x + dx2, y + dy2)]:
                        possible = False
                if possible:
                    pos_to_count[(x + dx, y + dy)] += 1
                    elf_to_next_pos[(x, y)] = (x + dx, y + dy)
                    break

        next_elves = []
        for x, y in elves:
            if (x, y) in elf_to_next_pos and pos_to_count[elf_to_next_pos[(x, y)]] == 1:
                x2, y2 = elf_to_next_pos[(x, y)]
                next_elves.append((x2, y2))
                grid[(x, y)] = False
                grid[(x2, y2)] = True
            else:
                next_elves.append((x, y))
        elves = next_elves
        first = moves.pop(0)
        moves.append(first)

    min_x = min([x for x, y in elves])
    max_x = max([x for x, y in elves])
    min_y = min([y for x, y in elves])
    max_y = max([y for x, y in elves])
    result = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if not grid[(x, y)]:
                result += 1

    return result


def read_input():
    return [line.strip() for line in sys.stdin]


inp = read_input()
print(step1(inp))