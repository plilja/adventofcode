import sys
import re
from collections import namedtuple
from math import *

Nanobot = namedtuple('Nanobot', 'x y z r')

def dist(n1, n2):
    return abs(n1.x - n2.x) + abs(n1.y - n2.y) + abs(n1.z - n2.z)


def step1(nanobots):
    strongest = max(nanobots, key=lambda n: n.r)
    in_range = list(filter(lambda n: dist(n, strongest) <= strongest.r, nanobots))
    return len(in_range)


def parse_input():
    r = []
    for s in sys.stdin:
        xs = list(map(int, re.findall(r'-?\d+', s)))
        r.append(Nanobot(xs[0], xs[1], xs[2], xs[3]))
    return r

nanobots = parse_input()
print(step1(nanobots)) 
