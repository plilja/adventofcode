def group(ls):
    """ Groups adjacent equal elements together,
    for example [1, 1, 2, 3, 3] becomes [[1, 1], [2], [3, 3]]
    """
    res = []
    prev = None
    for a in ls:
        if a != prev:
            res.append([a])
        else:
            res[-1].append(a)
        prev = a
    return res


def step1(start, end):
    res = 0
    for i in range(start, end + 1):
        s = str(i)
        a = len(s) == 6
        b = any(map(lambda x: len(x) >= 2, group(s)))
        c = all(map(lambda t: t[0] <= t[1], zip(s, s[1:])))
        res += 1 if a and b and c else 0
    return res


def step2(start, end):
    res = 0
    for i in range(start, end + 1):
        s = str(i)
        a = len(s) == 6
        b = any(map(lambda x: len(x) == 2, group(s)))
        c = all(map(lambda t: t[0] <= t[1], zip(s, s[1:])))
        res += 1 if a and b and c else 0
    return res


def main():
    [start, end] = list(map(int, input().split()))
    print(step1(start, end))
    print(step2(start, end))


if __name__ == '__main__':
    main()
