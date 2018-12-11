def power_level(serial_number, x, y):
    rack_id = x + 10
    tmp = rack_id * (rack_id * y + serial_number)
    return (tmp // 100) % 10 - 5


def step1(serial_number):
    r = 0
    rx = 0
    ry = 0
    for x in range(1, 301 - 3):
        for y in range(1, 301 - 3):
            s = 0
            for i in range(0, 3):
                for j in range(0, 3):
                    s += power_level(serial_number, x + i, y + j)
            if s > r:
                r = s
                rx = x
                ry = y
    return (rx, ry)


serial_number = int(input())
print(step1(serial_number))
