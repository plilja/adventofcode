import re
from common.math_util import sign


def step1(x1, x2, y1, y2):
    max_y, n = solve(x1, x2, y1, y2)
    return max_y


def step2(x1, x2, y1, y2):
    max_y, n = solve(x1, x2, y1, y2)
    return n


def solve(x1, x2, y1, y2):
    max_ys = []
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    for init_vel_x in range(-x1 - 1, x2 + 2):
        for init_vel_y in range(min(y1, 1), 2 * abs(y2) + 2):
            vel_x = init_vel_x
            vel_y = init_vel_y
            match = False
            max_y = 0
            x, y = 0, 0
            while x <= x2 and y1 <= y:
                x += vel_x
                y += vel_y
                vel_x -= sign(vel_x)
                vel_y -= 1
                max_y = max(y, max_y)
                if x1 <= x <= x2 and y1 <= y <= y2:
                    match = True
            if match:
                max_ys.append(max_y)
    return max(max_ys), len(max_ys)



def read_input():
    inp = input()
    args = re.match(r'target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)', inp).groups()
    return int(args[0]), int(args[1]), int(args[2]), int(args[3])


def main():
    args = read_input()
    print(step1(*args))
    print(step2(*args))


if __name__ == '__main__':
    main()
