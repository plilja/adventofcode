import sys
import math


def step1(inp):
    result = 0
    asteroids = []
    for y in range(0, len(inp)):
        for x in range(0, len(inp[0])):
            if inp[y][x] == '#':
                asteroids.append((x, y))
    for x1, y1 in asteroids:
        angles = []
        for x2, y2 in asteroids:
            if (x1, y1) != (x2, y2):
                angle = math.atan2(y2 - y1, x2 - x1)
                angles.append(angle)
        angles.sort()
        counter = 1
        for a1, a2 in zip(angles, angles[1:]):
            if abs(a1 - a2) > 1e-9:
                counter += 1
        result = max(result, counter)
    return result


inp = list(map(str.strip, sys.stdin.readlines()))
print(step1(inp))
