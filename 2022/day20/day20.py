import sys
from collections import deque


def shift(deq, value):
    deq2 = deque()

    def init_deq2():
        while deq[0] != value:
            deq2.append(deq.popleft())

    def shift_left():
        if deq2:
            deq.popleft()
            deq.appendleft(deq2.pop())
            deq.appendleft(value)
            if not deq2:
                shift_left()
        else:
            deq.popleft()
            deq.append(value)
            init_deq2()

    def shift_right():
        deq.popleft()
        if deq:
            deq2.append(deq.popleft())
            deq.appendleft(value)
        else:
            while deq2:
                deq.appendleft(deq2.pop())
            deq.appendleft(value)
            shift_right()

    v, i = list(map(int, value.split('|')))
    if v != 0:
        init_deq2()
        for _ in range(0, abs(v)):
            if v < 0:
                shift_left()
            else:
                shift_right()

    while deq2:
        deq.appendleft(deq2.pop())


def step1(inp):
    ls = deque()
    for i, v in enumerate(inp):
        if v == 0:
            zero_key = '{}|{}'.format(0, i)
        ls.append('{}|{}'.format(v, i))
    n = len(inp)
    cp = inp[::]
    for i, v in enumerate(inp):
        shift(ls, '{}|{}'.format(v, i))
    zero = ls.index(zero_key)
    result = 0
    for off in [1000, 2000, 3000]:
        result += int(ls[(zero + off) % n].split('|')[0])
    return result


if __name__ == '__main__':
    inp = list(map(int, sys.stdin.readlines()))
    print(step1(inp))
