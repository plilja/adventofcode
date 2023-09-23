import re
from math import gcd


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def forward(vs, dvs):
    for j in range(0, len(vs)):
        for k in range(0, len(vs)):
            if j == k:
                continue
            v1 = vs[j]
            v2 = vs[k]
            if v1 != v2:
                dvs[j] += 1 if v1 < v2 else -1
    for j in range(0, len(moons)):
        vs[j] += dvs[j]


def step1(moons):
    xs = [m[0] for m in moons]
    dxs = [0 for _ in range(0, 4)]
    ys = [m[1] for m in moons]
    dys = [0 for _ in range(0, 4)]
    zs = [m[2] for m in moons]
    dzs = [0 for _ in range(0, 4)]
    for i in range(0, 1000):
        forward(xs, dxs)
        forward(ys, dys)
        forward(zs, dzs)
    result = 0
    for i in range(0, 4):
        result += (abs(xs[i]) + abs(ys[i]) + abs(zs[i])) * (abs(dxs[i]) + abs(dys[i]) + abs(dzs[i]))
    return result


def step2(moons):
    result = 1
    for i in range(0, 3):
        vs = [m[i] for m in moons]
        dvs = [0 for _ in range(0, 4)]
        first = (tuple(vs), tuple(dvs))
        i = 0
        while i == 0 or first != (tuple(vs), tuple(dvs)):
            forward(vs, dvs)
            i += 1
        result = lcm(result, i)
    return result


def read_moon():
    [x, y, z] = re.match(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>.*', input()).groups()
    return int(x), int(y), int(z)


moons = [read_moon() for _ in range(0, 4)]
print(step1(moons))
print(step2(moons))
