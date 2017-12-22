import sys
import re
from collections import namedtuple

Particle = namedtuple('Particle', 'position velocity acceleration')

def step1(particles):
    min_acc = float('inf')
    min_idx = -1
    min_point = None
    for i, particle in enumerate(particles):
        a1, a2, a3 = particle.acceleration
        acc = abs(a1) + abs(a2) + abs(a3)
        if acc <= min_acc:
            # Should consider velocity and initial position to be certain
            # in case acceleration is equal. But this is good enough for
            # the test input
            min_acc = acc
            min_idx = i
    return min_idx


def get_input():
    res = []
    for s in sys.stdin:
        p, v, a = re.match(r'p=<([^>]*)>, v=<([^>]*)>, a=<([^>]*)>', s).groups()
        res += [Particle(ints(p), ints(v), ints(a))]
    return res


def ints(s):
    return tuple(map(int, s.split(',')))


particles = get_input()
print(step1(particles))
