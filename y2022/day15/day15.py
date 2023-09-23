import sys
import re


def step1(sensors):
    target_y = 2000000
    intervals = []
    for ((sx, sy), (bx, by)) in sensors:
        dist_to_beacon = abs(sx - bx) + abs(sy - by)
        rem_dist = dist_to_beacon - abs(target_y - sy)
        intervals.append((sx - rem_dist, sx + rem_dist))
    intervals.sort()
    prev = float('-inf')
    result = 0
    for (start, end) in intervals:
        if end > prev:
            result += end - max(start, prev)
            prev = end
    return result


def step2(sensors):
    lim = 4000000
    for y in range(0, lim + 1):
        intervals = []
        for ((sx, sy), (bx, by)) in sensors:
            dist_to_beacon = abs(sx - bx) + abs(sy - by)
            rem_dist = dist_to_beacon - abs(y - sy)
            intervals.append((sx - rem_dist, sx + rem_dist))
        intervals.sort()
        prev = -1
        for (start, end) in intervals:
            if prev + 1 < start and 0 <= prev <= lim:
                return tuning_freq(prev + 1, y)
            prev = max(prev, end)
        if prev < lim:
            return tuning_freq(prev + 1, y)

    raise ValueError('Unable to locate beacon')


def tuning_freq(x, y):
    return x * 4000000 + y


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
print('This one is slow. Wait for it...', file=sys.stderr)
print(step2(sensors))
