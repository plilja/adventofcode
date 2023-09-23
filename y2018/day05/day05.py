def step1(inp):
    left = list(inp)
    right = []
    while left:
        a = left.pop()
        if not right:
            right.append(a)
        else:
            b = right[-1]
            if a != b and a.upper() == b.upper():
                right.pop()
            else:
                right.append(a)
    return len(right)


def step2(inp):
    units = set(list(inp.lower()))
    lengths = [step1(inp.replace(x, '').replace(x.upper(), '')) for x in units]
    return min(lengths)


inp = input()
print(step1(inp))
print(step2(inp))
