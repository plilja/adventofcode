x = 0
y = 0
dx = 0
dy = -1 # face north initially
for inp in input().replace(',', '').split():
    if inp[0] == 'L':
        dx, dy = dy, -dx
    else:
        dx, dy = -dy, dx
    steps = int(inp[1:])
    x += steps * dx
    y += steps * dy

print(abs(x) + abs(y))



