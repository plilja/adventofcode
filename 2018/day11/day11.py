def power_level(serial_number, x, y):
    rack_id = x + 10
    tmp = rack_id * (rack_id * y + serial_number)
    return (tmp // 100) % 10 - 5


def step1(serial_number):
    x, y, _ = solve(serial_number, 3, 3)
    return (x, y)


def step2(serial_number):
    return solve(serial_number, 1, 300)


def solve(serial_number, min_size, max_size):
    # grid[y][x] stores the sum of the grid bounded by (1, 1) to (x, y)
    grid = [[0 for j in range(0, 302)] for i in range(0, 302)]
    for y in range(1, 301):
        s = 0
        for x in range(1, 301):
            s += power_level(serial_number, x, y)
            grid[y][x] = grid[y - 1][x] + s

    r, rz, ry, rz = 0, 0, 0, 0
    for z in range(min_size, max_size + 1):
        for y in range(1, 301 - z):
            s = 0
            for x in range(1, 301 - z):
                s = grid[y + z - 1][x + z - 1] - grid[y + z - 1][x - 1] - grid[y - 1][x + z - 1] + grid[y - 1][x - 1]
                if s > r:
                    r = s
                    rx = x
                    ry = y
                    rz = z
    return (rx, ry, rz)


serial_number = int(input())
print(step1(serial_number))
print(step2(serial_number)) 
