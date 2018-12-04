import sys
import re
from datetime import datetime
from collections import *


class Guard():
    def __init__(self, nr):
        self.nr = nr
        self.sleep_minutes = Counter()


    def sleep(self, timestamp):
        minute = timestamp.time().minute
        self.sleep_start = minute


    def wake(self, timestamp):
        wake_minute = timestamp.time().minute
        for m in range(self.sleep_start, wake_minute):
            self.sleep_minutes[m] += 1


    def total_sleep(self):
        return sum(self.sleep_minutes.values())


    def most_slept_minute(self):
        if len(self.sleep_minutes) > 0:
            return self.sleep_minutes.most_common(1)[0][0]
        else:
            return 0


    def times_slept_on_minute(self, m):
        if len(self.sleep_minutes) > 0:
            return self.sleep_minutes[m]
        else:
            return 0


class Records():
    def __init__(self, records):
        self.guards = {}
        guard = None
        log = []
        for line in inp:
            ts_tmp, command = re.match(r'\[(.*)\] (.*)', line).groups()
            ts = datetime.strptime(ts_tmp, '%Y-%m-%d %H:%M')
            log += [(ts, command)]
        log.sort()

        for ts, command in log:
            if command == 'falls asleep':
                guard.sleep(ts)
            elif command == 'wakes up':
                guard.wake(ts)
            else:
                assert command.startswith('Guard ')
                nr, = re.match(r'Guard #(\d+) begins shift', command).groups()
                nr = int(nr)
                guard = self.guards.setdefault(nr, Guard(nr))


    def sleepiest_guard(self):
        return max(self.guards.values(), key=lambda g: g.total_sleep())


    def guard_sleeps_on_same_minute(self):
        return max(self.guards.values(), key=lambda g: g.times_slept_on_minute(g.most_slept_minute()))


def step1(inp):
    records = Records(inp)
    guard = records.sleepiest_guard()
    return guard.nr * guard.most_slept_minute()


def step2(inp):
    records = Records(inp)
    guard = records.guard_sleeps_on_same_minute()
    return guard.nr * guard.most_slept_minute()


inp = sys.stdin.readlines()
print(step1(inp))
print(step2(inp))
