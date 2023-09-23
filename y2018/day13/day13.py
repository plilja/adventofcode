import sys


def step1(inp):
    crashes, remaining = solve(inp, lambda num_carts: 1)
    return crashes[0]


def step2(inp):
    crashes, remaining = solve(inp, lambda num_carts: num_carts // 2)
    return remaining[0]


def solve(inp, num_crashes_allowed_func):
    # parse carts
    carts = {}
    for y in range(0, len(inp)):
        for x in range(0, len(inp[y])):
            c = inp[y][x]
            if c == '<':
                carts[(x, y)] = (-1, 0, 0)
            elif c == '>':
                carts[(x, y)] = (1, 0, 0)
            elif c == '^':
                carts[(x, y)] = (0, -1, 0)
            elif c == 'v':
                carts[(x, y)] = (0, 1, 0)

    crashes = []
    num_crashes_allowed = num_crashes_allowed_func(len(carts.keys()))
    while len(crashes) < num_crashes_allowed:
        for (x, y) in sorted(carts.keys(), key=lambda c: (c[1], c[0])):
            if (x, y) not in carts:
                # has crashed in previous loop step
                continue
            c = inp[y][x]
            dx, dy, turns = carts[(x, y)]
            if c == '+':
                r = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                idx = r.index((-dx, -dy))  # Idx of previous place
                dx, dy = r[(idx + 1 + (turns % 3)) % 4]
                turns += 1
            elif c == '\\':
                dx, dy = dy, dx
            elif c == '/':
                dx, dy = -dy, -dx
            else:
                assert c in ['-', '<', '>', '|', '^', 'v']  # dx, dy is unchanged

            x2 = x + dx
            y2 = y + dy
            if (x2, y2) in carts:
                del carts[(x, y)]
                del carts[(x2, y2)]
                crashes.append((x2, y2))
            else:
                del carts[(x, y)]
                carts[(x2, y2)] = (dx, dy, turns)

    return crashes, list(carts.keys())


inp = sys.stdin.readlines()
print(step1(inp))
print(step2(inp))
