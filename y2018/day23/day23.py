import sys
import re
import heapq
from collections import namedtuple
from math import *

Nanobot = namedtuple('Nanobot', 'x y z r')
Box = namedtuple('Box', 'x y z side')
Point = namedtuple('Point', 'x y z')


def dist_between_bots(bot1, bot2):
    return abs(bot1.x - bot2.x) + abs(bot1.y - bot2.y) + abs(bot1.z - bot2.z)


def step1(nanobots):
    strongest = max(nanobots, key=lambda n: n.r)
    in_range = list(filter(lambda n: dist_between_bots(
        n, strongest) <= strongest.r, nanobots))
    return len(in_range)


def step2(bots):
    """A* search the box that covers the most bots
       until we reach a box with side 1. Then we have the answer."""
    pq = [(-len(bots), 0, bounds(bots))]
    centre = Point(0, 0, 0)
    while pq:
        count, d, box = heapq.heappop(pq)
        if box.side == 1:
            return '%d bots are in range at distance ans=%d (point=%d,%d,%d)' % (-count, d, box.x, box.y, box.z)
        for sub_box in split_box(box):
            sub_count = count_bots_in_box(sub_box, bots)
            sub_dist = dist(sub_box, centre)
            heapq.heappush(pq, (-sub_count, sub_dist, sub_box))


def split_box(box):
    """Splits a box into 8 equal sized sub boxes"""
    assert box.side % 2 == 0
    x = box.x
    y = box.y
    z = box.z
    side = box.side // 2
    return [
        Box(x, y, z, side),
        Box(x + side, y, z, side),
        Box(x, y + side, z, side),
        Box(x + side, y + side, z, side),
        Box(x, y, z + side, side),
        Box(x + side, y, z + side, side),
        Box(x, y + side, z + side, side),
        Box(x + side, y + side, z + side, side),
    ]


def count_bots_in_box(box, bots):
    r = 0
    for bot in bots:
        if box_covers_bot(box, bot):
            r += 1
    return r


def box_covers_bot(box, bot):
    """Tells if a any point in a box is in range
    of a nanobot"""
    return dist(box, bot) <= bot.r


def dist(box, point):
    """Calculates Manhattan distance between a box and 
    a point (a point might be a nanobot)"""
    def h(t1, t2, p):
        if t1 <= p <= t2:
            return 0
        else:
            return min(abs(t1 - p), abs(t2 - p))

    xmin = box.x
    xmax = box.x + box.side - 1
    ymin = box.y
    ymax = box.y + box.side - 1
    zmin = box.z
    zmax = box.z + box.side - 1
    return h(xmin, xmax, point.x) + h(ymin, ymax, point.y) + h(zmin, zmax, point.z)


def bounds(bots):
    xs = list(map(lambda bot: bot.x, bots))
    ys = list(map(lambda bot: bot.y, bots))
    zs = list(map(lambda bot: bot.z, bots))
    xside = max(xs) - min(xs)
    yside = max(ys) - min(ys)
    zside = max(zs) - min(zs)
    maxside = max(xside, yside, zside)
    side = 2 ** (int(log(maxside, 2) + 1))
    x = min(xs)
    y = min(ys)
    z = min(zs)
    return Box(x, y, z, side)


def parse_input():
    r = []
    for s in sys.stdin:
        xs = list(map(int, re.findall(r'-?\d+', s)))
        r.append(Nanobot(xs[0], xs[1], xs[2], xs[3]))
    return r


def main():
    nanobots = parse_input()
    print(step1(nanobots))
    print(step2(nanobots))


if __name__ == '__main__':
    main()
