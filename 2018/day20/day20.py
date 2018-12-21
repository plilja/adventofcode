from collections import defaultdict, deque
import sys

def step1(inp):
    grid = defaultdict(lambda: defaultdict(lambda: '#'))

    def group(s, i):
        assert s[i] == '('
        balance = 1
        j = i + 1
        sub = ''
        r = []
        while j < len(s) and balance != 0:
            c = s[j]
            if c == '(':
                balance += 1
                sub += c
            elif c == ')':
                balance -= 1
                if balance != 0:
                    sub += c
            elif c == '|' and balance == 1:
                r.append(sub)
                sub = ''
            else:
                sub += c
            j += 1
        r.append(sub)
        return r, j


    def parse(s, x, y, i, v):
        if (x, y, i, s) in v:
            return []
        grid[y][x] = '.'
        if i >= len(s):
            return [(x, y)]

        c = s[i]
        r = []
        if c == 'N':
            grid[y + 1][x] = '-'
            r += parse(s, x, y + 2, i + 1, v)
        elif c == 'S':
            grid[y - 1][x] = '-'
            r += parse(s, x, y - 2, i + 1, v)
        elif c == 'W':
            grid[y][x - 1] = '|'
            r += parse(s, x - 2, y, i + 1, v)
        elif c == 'E':
            grid[y][x + 1] = '|'
            r += parse(s, x + 2, y, i + 1, v)
        elif c == '(':
            options, j = group(s, i)
            for option in options:
                for x2, y2 in parse(option, x, y, 0, v):
                    r += parse(s, x2, y2, j, v)
        v[(x, y, i, s)] = r
        return r

    v = {}
    parse(inp, 0, 0, 0, v)

    # bfs
    q = deque([(0, 0, 0)])
    v = set()
    r = 0
    while q:
        x, y, d = q.popleft()
        if (x, y) in v:
            continue
        v |= {(x, y)}
        r = max(r, d)
        for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if grid[y + dy][x + dx] in '-|':
                q.append((x + 2 * dx, y + 2 * dy, d + 1))
    return r


sys.setrecursionlimit(10000)
inp = input().strip()[1:-1]
print(step1(inp)) 
