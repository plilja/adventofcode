import sys
import re


def step1(sensors):
    target_y = 2000000
    non_beacon = set()
    for ((sx, sy), (bx, by)) in sensors:
        dist_to_beacon = abs(sx - bx) + abs(sy - by)
        for x in range(sx - dist_to_beacon, sx + dist_to_beacon + 1):
            dist = abs(sx - x) + abs(sy - target_y)
            if dist <= dist_to_beacon and (x, target_y) != (bx, by):
                non_beacon.add((x, target_y))
    return len(non_beacon)


def read_input():
    result = []
    for line in sys.stdin:
        [x1, y1, x2, y2] = re.match(
            'Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)', line
        ).groups()
        result.append(((int(x1), int(y1)), (int(x2), int(y2))))
    return result


sensors = read_input()
print(step1(sensors))

