import sys
import re
from collections import namedtuple

Move = namedtuple('Move', 'fr to num')


def step1(stacks, moves):
    stacks_copy = [stack[::] for stack in stacks]
    for move in moves:
        for i in range(0, move.num):
            x = stacks_copy[move.fr].pop()
            stacks_copy[move.to].append(x)
    return top_of_stacks(stacks_copy)


def step2(stacks, moves):
    stacks_copy = [stack[::] for stack in stacks]
    for move in moves:
        lifted = []
        for i in range(0, move.num):
            x = stacks_copy[move.fr].pop()
            lifted.append(x)
        lifted.reverse()
        stacks_copy[move.to] += lifted
    return top_of_stacks(stacks_copy)


def top_of_stacks(stacks):
    result = []
    for stack in stacks:
        if stack:
            result.append(stack[-1])
    return ''.join(result)


def read_input():
    inp = sys.stdin.readlines()
    stacks = []
    moves = []
    for line in inp:
        if '[' in line:
            for i in range(1, len(line), 4):
                if len(stacks) == i // 4:
                    stacks.append([])
                if line[i] != ' ':
                    stacks[i // 4].append(line[i])
        elif 'move' in line:
            num, fr, to = re.match(r'move (\d+) from (\d+) to (\d+)', line).groups()
            moves.append(Move(int(fr) - 1, int(to) - 1, int(num)))
    for stack in stacks:
        stack.reverse()
    return stacks, moves


stacks, moves = read_input()
print(step1(stacks, moves))
print(step2(stacks, moves))
