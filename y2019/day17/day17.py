from collections import defaultdict
from y2019.intcode import IntcodeProcess


def read_space(instructions):
    process = IntcodeProcess(instructions)
    process.run_until_complete()
    space = defaultdict(lambda: defaultdict(lambda: '.'))
    x = 0
    y = 0
    while process.has_output():
        o = process.pop_output()
        if o == ord('\n'):
            x = 0
            y += 1
        else:
            space[y][x] = chr(o)
            x += 1
    return space


def step1(instructions):
    deltas = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    space = read_space(instructions)
    result = 0
    for y in list(space.keys()):
        for x in list(space[y].keys()):
            if all([space[y + dy][x + dx] == '#' for dx, dy in deltas]):
                result += x * y
    return result


def find_robot(space):
    for y in list(space.keys()):
        for x in list(space[y].keys()):
            if space[y][x] in ['^', '<', '>', 'v']:
                return x, y
    raise ValueError("Couldn't find robot")


def find_path(space):
    x, y = find_robot(space)
    deltas = {
        '^': (0, -1),
        '<': (-1, 0),
        '>': (1, 0),
        'v': (0, 1)
    }
    turns = {
        ('^', '<'): 'L',
        ('^', '>'): 'R',
        ('<', 'v'): 'L',
        ('<', '^'): 'R',
        ('>', '^'): 'L',
        ('>', 'v'): 'R',
        ('v', '>'): 'L',
        ('v', '<'): 'R'
    }
    # Find the path from start to finish, in theory there could be multiple
    # paths. But visual inspections yields that there is clearly a superior
    # path which is found by walking as long as possible and only turning
    # when needed.
    path = []
    old_direction = space[y][x]
    while True:
        for direction in ['^', '<', '>', 'v']:
            dx, dy = deltas[direction]
            length = 1
            while space[y + length * dy][x + length * dx] == '#':
                length += 1
            length -= 1
            if length > 0 and (old_direction, direction) in turns:
                x += length * dx
                y += length * dy
                turn = turns[(old_direction, direction)]
                path.append(turn)
                path.append(length)
                old_direction = direction
                break
        if length == 0:
            # No way to turn? Then we are finished
            break
    return path


def determine_movement_functions(path):
    assert len(path) > 3 * 20
    for i in range(1, 21):
        a = path[0:i]
        a_rem = path
        while a == a_rem[0:i]:
            a_rem = a_rem[i:]
        for j in range(1, 21):
            b = a_rem[0:j]
            b_rem = a_rem
            while b == b_rem[0:j]:
                b_rem = b_rem[j:]
            for k in range(1, 21):
                c = b_rem[0:k]
                assert b != c
                walk = []
                rem = path
                while len(rem) > 0:
                    if len(a) <= len(rem) and rem[0:len(a)] == a:
                        rem = rem[len(a):]
                        walk.append('A')
                        continue
                    if len(b) <= len(rem) and rem[0:len(b)] == b:
                        rem = rem[len(b):]
                        walk.append('B')
                        continue
                    if len(c) <= len(rem) and rem[0:len(c)] == c:
                        rem = rem[len(c):]
                        walk.append('C')
                        continue
                    break
                if not rem:
                    return walk, a, b, c


def input_list(process, ls):
    for i in range(0, len(ls)):
        for s in str(ls[i]):
            process.add_input(ord(s))
        if i < len(ls) - 1:
            process.add_input(ord(','))
        else:
            process.add_input(ord('\n'))


def step2(instructions):
    space = read_space(instructions)
    path = find_path(space)
    walk, a, b, c = determine_movement_functions(path)
    instructions[0] = 2
    process = IntcodeProcess(instructions)
    input_list(process, walk)
    input_list(process, a)
    input_list(process, b)
    input_list(process, c)
    process.add_input(ord('n'))
    process.add_input(ord('\n'))
    process.run_until_complete()
    return process.output[-1]


def main():
    instructions = list(map(int, input().split(',')))
    print(step1(instructions))
    print(step2(instructions))


if __name__ == '__main__':
    main()
