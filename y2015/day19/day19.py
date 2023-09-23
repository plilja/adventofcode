INF = float('inf')


def read_transitions():
    transitions = []
    while True:
        s = input()
        if s == "":
            return transitions
        else:
            [fr, _, to] = s.split()
            transitions += [(fr, to)]


def read_molecule():
    return input()


def step1(transitions, molecule):
    if not transitions:
        return set()
    else:
        (fr, to) = transitions[0]
        i = molecule.find(fr, 0)
        res = set()
        while i != -1:
            res |= {molecule[:i] + to + molecule[i + len(fr):]}
            i = molecule.find(fr, i + 1)
        return res | step1(transitions[1:], molecule)


# this is sort of cheating but there is no way that we can try
# all possible paths in a reasonable amount of time
def dfs(transitions, curr, v={}):
    if curr == 'e':
        return 0
    if curr in v:
        return v[curr]

    v[curr] = INF
    for fr, to in transitions:
        i = curr.find(to, 0)
        while i != -1:
            _next = curr[:i] + fr + curr[i + len(to):]
            sub = dfs(transitions, _next, v)
            if sub < INF:
                v[curr] = sub + 1
                return sub + 1
            i = curr.find(to, i + 1)
    return INF


g = read_transitions()
molecule = read_molecule()

print(len(step1(g, molecule)))
print(dfs(g, molecule))
