import sys
import re
from collections import *
from math import *
from queue import PriorityQueue

microchip_re = re.compile('\w+-compatible microchip')
generator_re = re.compile('\w+ generator')

INF = float('inf')

def step1(inp):
    def parse_floors():
        floors = [frozenset() for i in range(0, 4)]
        for i in range(0, len(inp)):
            line = inp[i]
            items = floors[i]
            for microchip in microchip_re.findall(line):
                element = microchip.split('-')[0]
                items = items | {'m_' + element}
            for generator in generator_re.findall(line):
                element = generator.split(' ')[0]
                items = items | {'g_' + element}
            floors[i] = (items)
        return tuple(floors)

    def is_done(floors):
        for items in floors[0:3]:
            if len(items) > 0:
                return False
        return True

    def is_generator(item):
        return item.startswith('g_')

    def is_microship(item):
        return item.startswith('m_')

    def element(item):
        return item[2:]

    def matching_item(item):
        if is_microship(item):
            return 'g_' + element(item)
        else:
            return 'm_' + element(item)

    def is_stable(items):
        has_generator = False
        for item in items:
            if is_generator(item):
                has_generator = True
                break
        if has_generator:
            for item in items:
                if is_microship(item) and not matching_item(item) in items:
                    return False
        return True

    def pick_one_or_two(items):
        r = []
        items_list = list(items)
        for i in range(0, len(items_list)):
            r += [{items_list[i]}]
            for j in range(i + 1, len(items_list)):
                r += [{items_list[i], items_list[j]}]
        return r

    def solve(initial_floors):
        visited = set()
        queue = PriorityQueue()
        queue.put((0, initial_floors, 0))
        while queue:
            dist, floors, current_floor = queue.get()

            if is_done(floors):
                return dist

            if (current_floor, floors) in visited:
                continue
            visited |= {(current_floor, floors)}

            items = floors[current_floor]
            for pick in pick_one_or_two(items):
                new_items = items - pick 
                if is_stable(pick) and is_stable(new_items):
                    for floor in range(0, 4):
                        if floor == current_floor:
                            continue
                        possible_move = True
                        h = int(copysign(1, floor - current_floor))
                        for k in range(current_floor + h, floor + h, h):
                            if not is_stable(floors[k] | pick):
                                possible_move = False
                                break
                        if possible_move:
                            new_floors = floors[:current_floor] + (new_items,) + floors[current_floor + 1:]
                            new_floors = new_floors[:floor] + (new_floors[floor] | pick,) + new_floors[floor + 1:]
                            queue.put((dist + abs(floor - current_floor), new_floors, floor))

        return INF # unsolvable

    return solve(parse_floors())

inp = sys.stdin.readlines()
print('This one is slow. Wait for it...', file=sys.stderr)
print('Step 1')
print(step1(inp))
