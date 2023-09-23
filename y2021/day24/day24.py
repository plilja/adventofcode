import sys


def step1(instructions):
    return solve(instructions, max)


def step2(instructions):
    return solve(instructions, min)


def solve(instructions, tie_breaker):
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
                        new_z = z
                    else:
                        new_z = z * 26 + w + off
                    if new_z not in new_states or tie_breaker(w, new_states[new_z][-1]) == w:
                        new_states[new_z] = inp + [w]
        if div == 26:
            num_divs -= 1
        states = new_states
    return ''.join(map(str, states[0]))


inp = [s.strip() for s in sys.stdin]
print(step1(inp))
print(step2(inp))
