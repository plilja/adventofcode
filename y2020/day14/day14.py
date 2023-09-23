import sys
import re
from collections import defaultdict
from enum import Enum
import copy


class Operations(Enum):
    MASK = 1
    MEM = 2


def step1(instructions):
    memory = defaultdict(int)
    mask0 = 0
    mask1 = int('1' * 36, 2)
    for instruction in instructions:
        if instruction[0] == Operations.MASK:
            m = instruction[1]
            mask0 = int(m.replace('X', '1'), 2)
            mask1 = int(m.replace('X', '0'), 2)
        else:
            assert instruction[0] == Operations.MEM
            memory[instruction[1]] = (instruction[2] & mask0) | mask1
    return sum(memory.values())


def step2(instructions):
    memory = {}
    mask = 0
    for instruction in instructions:
        if instruction[0] == Operations.MASK:
            mask = instruction[1]
        else:
            assert instruction[0] == Operations.MEM
            addr = list(('0' * 36 + bin(instruction[1])[2:])[-36:])
            # Ugly stuff below. Probably exists some nicer solution...

            def set_val(node, i):
                if i == 36:
                    node['VAL'] = instruction[2]
                    return
                bit = mask[i]
                if bit in ['0', '1']:
                    val = '1' if bit == '1' else addr[i]
                    if 'X' in node:
                        assert '0' not in node
                        assert '1' not in node
                        tmp = node['X']
                        node['0' if val == '1' else '1'] = tmp
                        node[val] = copy.deepcopy(tmp)
                        del node['X']

                    if val not in node:
                        node[val] = {}
                    set_val(node[val], i + 1)
                else:
                    assert bit == 'X'
                    if '0' in node and '1' in node:
                        set_val(node['0'], i + 1)
                        set_val(node['1'], i + 1)
                    elif '0' in node:
                        assert '1' not in node
                        set_val(node['0'], i + 1)
                        node['1'] = {}
                        set_val(node['1'], i + 1)
                    elif '1' in node:
                        assert '0' not in node
                        set_val(node['1'], i + 1)
                        node['0'] = {}
                        set_val(node['0'], i + 1)
                    else:
                        assert '0' not in node
                        assert '1' not in node
                        if 'X' not in node:
                            node['X'] = {}
                        set_val(node['X'], i + 1)
            set_val(memory, 0)

    def count(node):
        if 'VAL' in node:
            return node['VAL']
        elif 'X' in node:
            return 2 * count(node['X'])
        else:
            return sum([count(x) for x in node.values()])
    return count(memory)


def read_instructions():
    result = []
    for line in sys.stdin:
        m1 = re.match(r'mem\[(\d+)\] = (\d+)', line)
        if m1:
            a, b = m1.groups()
            result.append((Operations.MEM, int(a), int(b)))
        else:
            m2 = re.match(r'mask = ([\dX]+)', line)
            assert m2
            c = m2.groups()[0]
            result.append((Operations.MASK, c))
    return result


instructions = read_instructions()
print(step1(instructions))
print(step2(instructions))
