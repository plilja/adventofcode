
directions = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, -1),
        'D': (0, 1)
    }


def walk(wire):
    x, y = 0, 0
    res = set()
    for step in wire:
        dx, dy = directions[step[0]]
        length = int(step[1:])
        for i in range(0, length):
            x += dx
            y += dy
            res.add((x, y))
    return res


def step1(wire1, wire2):
    locations1 = walk(wire1)
    locations2 = walk(wire2)
    min_dist = float('inf')
    for location in locations1:
        if location in locations2:
            min_dist = min(min_dist, abs(location[0]) + abs(location[1]))
    return min_dist


wire1 = input().split(',')
wire2 = input().split(',')
print(step1(wire1, wire2))
