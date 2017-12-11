from collections import defaultdict

def step1(inp):
    directions = inp.split(',')
    process_x, process_y = 0, 0
    for dr in directions:
        if dr == 'n':
            dx, dy = -1, -1
        elif dr == 'ne':
            dx, dy = 0, -1
        elif dr == 'se':
            dx, dy = 1, 0
        elif dr == 's':
            dx, dy = 1, 1
        elif dr == 'sw':
            dx, dy = 0, 1
        elif dr == 'nw':
            dx, dy = -1, 0
        process_x += dx
        process_y += dy
    if (process_x < 0 and process_y < 0) or (process_x > 0 and process_y > 0):
        return max(abs(process_x), abs(process_y))
    else:
        return abs(process_x) + abs(process_y)


inp = input()
print(step1(inp))
