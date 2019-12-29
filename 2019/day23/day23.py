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


def step2(instructions):
    computers = []
    for nic in range(0, 50):
        computer = IntcodeProcess(instructions)
        computer.add_input(nic)
        computers.append(computer)
    nat_deliverys = set()
    nat = None
    while True:
        for computer in computers:
            while not computer.needs_input():
                computer.tick()

        for computer in computers:
            if len(computer.output) >= 3:
                d = computer.pop_output()
                x = computer.pop_output()
                y = computer.pop_output()
                if d == 255:
                    nat = (x, y)
                else:
                    computers[d].add_input(x)
                    computers[d].add_input(y)

        idle = True
        for computer in computers:
            idle = idle and computer.needs_input()
            idle = idle and not computer.has_output()

        if idle and nat:
            computers[0].add_input(nat[0])
            computers[0].add_input(nat[1])
            if nat[1] in nat_deliverys:
                return nat[1]
            nat_deliverys.add(nat[1])
        for computer in computers:
            if computer.needs_input():
                computer.add_input(-1)


instructions = list(map(int, input().split(',')))
print(step1(instructions))
print(step2(instructions))
