import sys
from collections import deque, defaultdict


def solve(points):
    g = defaultdict(list)
    for i in range(len(points)):
        p1 = points[i]
        for j in range(i + 1, len(points)):
            p2 = points[j]
            d = 0
            for k in range(0, len(p1)):
                d += abs(p1[k] - p2[k])
            if d <= 3:
                g[i].append(j)
                g[j].append(i)

    v = set()
    r = 0
    for i in range(len(points)):
        if i in v:
            continue
        r += 1
        q = deque([i])
        while q:
            j = q.popleft()
            if j in v:
                continue
            v.add(j)
            for k in g[j]:
                q.append(k)
    return r


def main():
    points = [tuple(map(int, s.strip().split(','))) for s in sys.stdin]
    print(solve(points))
    # No step 2 this day


if __name__ == '__main__':
    main()
