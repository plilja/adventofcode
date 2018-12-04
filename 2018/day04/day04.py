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
        return self.sleep_minutes.most_common(1)[0][0]


    def times_slept_on_minute(self, m):
        return self.sleep_minutes[m]


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
                if nr not in self.guards:
                    self.guards[nr] = Guard(nr)
                guard = self.guards[nr]


    def sleepiest_guard(self):
        best = 0
        guard = None
        for g in self.guards.values():
            if g.total_sleep() > best:
                guard = g
                best = g.total_sleep()
        return guard


    def guard_sleeps_on_same_minute(self):
        best = 0
        guard = None
        for g in self.guards.values():
            if g.total_sleep() > 0:
                m = g.most_slept_minute()
                t = g.times_slept_on_minute(m)
                if t > best:
                    guard = g
                    best = t
        return guard



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
