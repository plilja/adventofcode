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


inp = input()
print(step1(inp))
