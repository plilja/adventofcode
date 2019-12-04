def step1(start, end):
    res = 0
    for i in range(start, end + 1):
        s = str(i)
        a = len(s) == 6
        b = any(map(lambda t: t[0] == t[1], zip(s, s[1:])))
        c = all(map(lambda t: t[0] <= t[1], zip(s, s[1:])))
        res += 1 if a and b and c else 0
    return res


[start, end] = list(map(int, input().split()))
print(step1(start, end))
