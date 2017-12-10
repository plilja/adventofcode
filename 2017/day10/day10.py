M = 256

def step1(inp):
    ls = [i for i in range(0, M)]
    skip = 0
    curr = 0
    for i in inp:
        rev(ls, curr, i)
        curr += i + skip
        skip += 1
    return ls[0] * ls[1]


def rev(ls, i, num):
    n = len(ls)
    for j in range(0, num // 2):
        tmp = ls[(i + j) % n]
        ls[(i + j) % n] = ls[(i + num - j - 1) % n]
        ls[(i + num - j - 1) % n] = tmp


inp = [int(s) for s in input().split(',')]
print(step1(inp))
