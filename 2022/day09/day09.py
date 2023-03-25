import sys

dirs = {
    'R': (1, 0),
    'L': (-1, 0),
    'D': (0, 1),
    'U': (0, -1)
}


def step1(inp):
    head = [0, 0]
    tail = [0, 0]
    visited = set()
    for dir, steps in inp:
        dx, dy = dirs[dir]
        for _ in range(0, steps):
            head[0] += dx
            head[1] += dy
            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                tail[0] = head[0] - dx
                tail[1] = head[1] - dy
            visited.add(tuple(tail))
    return len(visited)


inp = [(x.split()[0], int(x.split()[1])) for x in sys.stdin]
print(step1(inp))
