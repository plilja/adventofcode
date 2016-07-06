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


def solve(transitions, molecule):
    if transitions == []:
        return set()
    else:
        (fr, to) = transitions[0]
        i = molecule.find(fr, 0)
        res = set()
        while i != -1:
            res |= {molecule[:i] + to + molecule[i + len(fr):]}
            i = molecule.find(fr, i + 1)
        return res | solve(transitions[1:], molecule)


print(len(solve(read_transitions(), read_molecule())))
