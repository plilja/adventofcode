
def step1(n, target_x, target_y):
    queue = [(1, 1, 0)]
    visited = {(1, 1)}
    while queue:
        x, y, dist = queue[0]
        queue = queue[1:]

        if x == target_x and y == target_y:
            return dist

        neighbours = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
        for x2, y2 in neighbours:
            if is_open(n, x2, y2) and (x2, y2) not in visited:
                visited |= {(x2, y2)}
                queue += [(x2, y2, dist + 1)]

    return float('inf')


def is_open(n, x, y):
    k = x*x + 3*x + 2*x*y + y + y*y + n
    count = 0
    while k != 0:
        count += k & 1
        k >>= 1
    return count % 2 == 0


n = int(input())
[x, y] = list(map(int, input().split()))
print(step1(n, x, y))
