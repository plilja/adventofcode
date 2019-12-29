import sys
sys.path.append("..")
from collections import defaultdict
from intcode import IntcodeProcess


def step1(instructions):
    computers = []
    for nic in range(0, 50):
        computer = IntcodeProcess(instructions)
        computer.add_input(nic)
        computers.append(computer)
    while True:
        for computer in computers:
            computer.tick()
        for computer in computers:
            if len(computer.output) >= 3:
                d = computer.pop_output()
                x = computer.pop_output()
                y = computer.pop_output()
                if d == 255:
                    return y
                computers[d].add_input(x)
                computers[d].add_input(y)
        for computer in computers:
            if computer.needs_input():
                computer.add_input(-1)


instructions = list(map(int, input().split(',')))
print(step1(instructions))
