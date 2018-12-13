import sys

def step1(inp):
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

    while True:
        for (x, y) in sorted(carts.keys(), key=lambda c: (c[1], c[0])):
            c = inp[y][x]
            dx, dy, turns = carts[(x, y)]
            if c == '+':
                r = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                idx = r.index((-dx, -dy)) # Idx of previous place
                dx, dy = r[(idx + 1 + (turns % 3)) % 4]
                turns += 1
            elif c == '\\':
                dx, dy = dy, dx
            elif c == '/':
                dx, dy = -dy, -dx
            else:
                assert c in ['-', '<', '>', '|', '^', 'v'] # dx, dy is unchanged

            x2 = x + dx
            y2 = y + dy
            if (x2, y2) in carts:
                return (x2, y2)
            else:
                del carts[(x, y)]
                carts[(x2, y2)] = (dx, dy, turns)


inp = sys.stdin.readlines()
print(step1(inp))
