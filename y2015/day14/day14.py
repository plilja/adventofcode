import sys

TIME = 2503

reindeers = []
for i in sys.stdin.readlines():
    [reindeer, can, fly, speed, unit, _for1, num1, seconds1,
     but, then, must, rest, _for2, num2, seconds2] = i.split()
    reindeers += [(int(speed), int(num1), int(num2))]


def solve():
    timers = [reindeers[i][1] for i in range(0, len(reindeers))]
    dists = [0 for _ in reindeers]
    points = [0 for _ in reindeers]
    speeds = [reindeers[i][0] for i in range(0, len(reindeers))]
    for i in range(0, TIME):
        leaders = [0]
        for j in range(0, len(reindeers)):
            active_speed, num1, num2 = reindeers[j]
            timers[j] -= 1
            dists[j] += speeds[j]
            if timers[j] == 0:
                if speeds[j] == 0:
                    speeds[j] = active_speed
                    timers[j] = num1
                else:
                    speeds[j] = 0
                    timers[j] = num2
            if dists[j] > dists[leaders[0]]:
                leaders = [j]
            elif dists[j] == dists[leaders[0]] and j != leaders[0]:
                leaders += [j]

        for leader in leaders:
            points[leader] += 1

    winner_by_dist = max(dists)
    winner_by_points = max(points)
    return winner_by_dist, winner_by_points


def main():
    step1, step2 = solve()
    print(step1)
    print(step2)


if __name__ == '__main__':
    main()
