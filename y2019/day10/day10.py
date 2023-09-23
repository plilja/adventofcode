import sys
import math
from decimal import Decimal, getcontext


def get_astroids(inp):
    astroids = []
    for y in range(0, len(inp)):
        for x in range(0, len(inp[0])):
            if inp[y][x] == '#':
                astroids.append((x, y))
    return astroids


def get_astroid_angles_and_dists(astroids, x, y):
    angles = []
    for x2, y2 in astroids:
        if (x, y) != (x2, y2):
            dist = math.sqrt((y2 - y)**2 + (x2 - x)**2)
            angle = Decimal(math.atan2(y - y2, x - x2)) / 1
            angles.append((angle, dist, x2, y2))
    angles.sort()
    return angles


def step1(inp):
    result, rx, ry = 0, 0, 0
    astroids = get_astroids(inp)
    for x1, y1 in astroids:
        angles = list(map(lambda x: x[0], get_astroid_angles_and_dists(astroids, x1, y1)))
        counter = 1
        for a1, a2 in zip(angles, angles[1:]):
            if a1 != a2:
                counter += 1
        if counter > result:
            result = counter
            rx, ry = x1, y1
    return result, rx, ry


def step2(inp):
    _, x, y = step1(inp)
    astroids = get_astroids(inp)
    angles = get_astroid_angles_and_dists(astroids, x, y)
    straight_up = Decimal(math.atan2(1, 0)) / 1
    i = 0
    while angles[i][0] < straight_up:
        i += 1
    prev_angle = Decimal(float('inf'))
    vaporized = set()
    last_vaporized = None
    while len(vaporized) < 200:
        a, _, x2, y2 = angles[i]
        if (x2, y2) not in vaporized:
            if a != prev_angle:
                vaporized |= {(x2, y2)}
                last_vaporized = (x2, y2)
            prev_angle = a
        i = (i + 1) % len(angles)
    return 100 * last_vaporized[0] + last_vaporized[1]


def main():
    getcontext().prec = 8
    inp = list(map(str.strip, sys.stdin.readlines()))
    print(step1(inp)[0])
    print(step2(inp))


if __name__ == '__main__':
    main()
