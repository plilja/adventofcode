import re
from dataclasses import dataclass


@dataclass
class Moon:
    x: int
    y: int
    z: int
    dx: int
    dy: int
    dz: int


def step1(moons):
    for i in range(0, 1000):
        for j in range(0, len(moons)):
            for k in range(0, len(moons)):
                if j == k:
                    continue
                m1 = moons[j]
                m2 = moons[k]
                if m1.x != m2.x:
                    moons[j].dx += 1 if m1.x < m2.x else -1
                if m1.y != m2.y:
                    moons[j].dy += 1 if m1.y < m2.y else -1
                if m1.z != m2.z:
                    moons[j].dz += 1 if m1.z < m2.z else -1
        for j in range(0, len(moons)):
            moons[j].x += moons[j].dx
            moons[j].y += moons[j].dy
            moons[j].z += moons[j].dz

    result = 0
    for m in moons:
        result += (abs(m.x) + abs(m.y) + abs(m.z)) * (abs(m.dx) + abs(m.dy) + abs(m.dz))
    return result



def read_moon():
    [x, y, z] = re.match(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>.*', input()).groups()
    return Moon(int(x), int(y), int(z), 0, 0, 0)


moons = [read_moon() for _ in range(0, 4)]
print(step1(moons))
