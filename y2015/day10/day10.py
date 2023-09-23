def group(v):
    r = []
    t = []
    for i in v:
        if t == [] or t[0] == i:
            t += [i]
        else:
            r += [t]
            t = [i]

    if t:
        r += [t]

    return r


def f(s, i):
    if i == 0:
        return s
    else:
        t = ''
        for g in group(s):
            t += str(len(g)) + g[0]
        return f(t, i - 1)


inp = input()
print(len(f(inp, 40)))
print(len(f(inp, 50)))
