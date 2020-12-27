

def shift_leftmost(cups, target):
    while cups[0] != target:
        x = cups.pop(0)
        cups.append(x)


def step1(cups):
    highest = max(cups)
    for i in range(0, 100):
        pick_up = cups[1:4]
        cups = cups[:1] + cups[4:]
        next_current = cups[1]
        destination = cups[0]
        while True:
            destination -= 1
            if destination < 1:
                destination = highest
            if destination not in pick_up:
                break
        i = cups.index(destination)
        cups = cups[:i + 1] + pick_up + cups[i + 1:]
        shift_leftmost(cups, next_current)
    shift_leftmost(cups, 1)
    return ''.join(map(str, cups[1:]))


inp = [int(x) for x in input()]
print(step1(inp[::]))
