import sys
import re
from collections import namedtuple

Cube = namedtuple('Cube', 'on_off section_x section_y section_z')
Section = namedtuple('Section', 'p1 p2')


def step1(cubes):
    to_check = []
    for cube in cubes:
        if abs(cube.section_x.p1) <= 50:
            to_check.append(cube)
    return solve(to_check)


def step2(cubes):
    return solve(cubes)


def solve(cubes):
    result = 0
    for i in range(0, len(cubes)):
        if cubes[i].on_off == 'off':
            continue
        visible = [cubes[i]]
        for j in range(i + 1, len(cubes)):
            cube2 = cubes[j]
            tmp = []
            for cube1 in visible:
                tmp += split(cube1, cube2)
            visible = tmp
        for cube in visible:
            result += volume(cube)
    return result


def split(cube1, cube2):
    """Splits cube1 such that only sections that doesn't overlap cube2 remains"""
    result = []
    if not cube_has_overlap(cube1, cube2):
        result.append(cube1)
    else:
        for split_x in split_section(cube1.section_x, cube2.section_x):
            if not section_has_overlap(split_x, cube2.section_x):
                result.append(Cube(cube1.on_off, split_x, cube1.section_y, cube1.section_z))
            else:
                for split_y in split_section(cube1.section_y, cube2.section_y):
                    if not section_has_overlap(split_y, cube2.section_y):
                        result.append(Cube(cube1.on_off, split_x, split_y, cube1.section_z))
                    else:
                        for split_z in split_section(cube1.section_z, cube2.section_z):
                            if not section_has_overlap(split_z, cube2.section_z):
                                result.append(Cube(cube1.on_off, split_x, split_y, split_z))
    return result


def cube_has_overlap(cube1, cube2):
    """return true if some point (or many) in cube1 is inside of cube2"""
    return section_has_overlap(cube1.section_x, cube2.section_x) and \
        section_has_overlap(cube1.section_y, cube2.section_y) and \
        section_has_overlap(cube1.section_z, cube2.section_z)


def section_has_overlap(section1, section2):
    """return true if some point (or many) in section1 is inside of section2"""
    return not (section1.p2 < section2.p1) and not (section1.p1 > section2.p2)


def split_section(section1, section2):
    result = []
    if section1.p1 < section2.p1:
        result.append(Section(section1.p1, min(section1.p2, section2.p1 - 1)))
    if section_has_overlap(section1, section2):
        result.append(Section(max(section1.p1, section2.p1), min(section1.p2, section2.p2)))
    if section1.p2 > section2.p2:
        result.append(Section(max(section1.p1, section2.p2 + 1), section1.p2))
    return result


def volume(cube):
    return (abs(cube.section_x.p1 - cube.section_x.p2) + 1) * \
        (abs(cube.section_y.p1 - cube.section_y.p2) + 1) * \
        (abs(cube.section_z.p1 - cube.section_z.p2) + 1)


def read_input():
    result = []
    index = 0
    for line in sys.stdin:
        [on_off, x1, x2, y1, y2, z1, z2] = re.match(r'(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)', line).groups()
        section_x = Section(int(x1), int(x2))
        section_y = Section(int(y1), int(y2))
        section_z = Section(int(z1), int(z2))
        result.append(Cube(on_off, section_x, section_y, section_z))
        index += 1
    return result


cubes = read_input()
print(step1(cubes))
print(step2(cubes))
