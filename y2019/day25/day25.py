from y2019.intcode import IntcodeProcess
import itertools


def picks(values):
    result = []
    for i in range(0, len(values)):
        result += list(itertools.combinations(values, i))
    return result


def add_input(process, inp):
    for s in inp:
        process.add_input(ord(s))
    process.add_input(ord('\n'))


commands_to_pick_all_items = [
        'east', 'take weather machine', 'west', 'west', 'west',
        'take bowl of rice', 'east', 'north', 'take polygon', 'east',
        'take hypercube', 'south', 'take dark matter', 'north', 'west',
        'north', 'take candy cane', 'west', 'north', 'take manifold',
        'south', 'west', 'north', 'take dehydrated water', 'west',
        'drop manifold', 'drop dehydrated water', 'drop polygon',
        'drop weather machine', 'drop bowl of rice', 'drop hypercube',
        'drop candy cane', 'drop dark matter'
    ]


def solve(instructions):
    items = [
        'manifold',
        'dehydrated water',
        'polygon',
        'weather machine',
        'bowl of rice',
        'hypercube',
        'dark matter',
        'candy cane'
    ]
    p = picks(items)
    process = IntcodeProcess(instructions)
    for command in commands_to_pick_all_items:
        add_input(process, command)
    k = 0
    while True:
        while process.is_running() and not process.needs_input():
            process.tick()
        if process.has_output():
            o = []
            while process.has_output():
                o.append(process.pop_output())
            s = ''.join(list(map(chr, o)))
            if 'ejected back to the checkpoint' not in s and k > 0:
                return s[s.find('"Oh, hello! You should be able to get in by typing'):].split('\n')[0]
        if process.needs_input():
            if k > 0:
                for item in p[k - 1]:
                    add_input(process, 'drop ' + item)
            for item in p[k]:
                add_input(process, 'take ' + item)
            k += 1
            add_input(process, 'inv')
            add_input(process, 'south')


instructions = list(map(int, input().split(',')))
print(solve(instructions))
