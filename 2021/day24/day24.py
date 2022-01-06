import sys


def step1(instructions):
    args = []
    num_divs = 0
    for i in range(0, len(instructions), 18):
        assert instructions[i].split()[0] == 'inp'
        assert instructions[i].split()[1] == 'w'
        div = int(instructions[i + 4].split()[2])
        salt = int(instructions[i + 5].split()[2])
        off = int(instructions[i + 15].split()[2])
        if div == 26:
            num_divs += 1
        args.append((div, salt, off))

    states = {0: []}
    for div, salt, off in args:
        new_states = {}
        for z, inp in states.items():
            x = z % 26 + salt
            z //= div
            if z < 26 ** num_divs:
                for w in range(1, 10):
                    if w == x:
                        new_states[z] = inp + [w]
                    else:
                        new_states[z * 26 + w + off] = inp + [w]
        if div == 26:
            num_divs -= 1
        states = new_states
    return ''.join(map(str, states[0]))


inp = [s.strip() for s in sys.stdin]
print(step1(inp))
