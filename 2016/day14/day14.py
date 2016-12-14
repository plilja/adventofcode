import hashlib
from collections import defaultdict


def step1(salt):
    i = 0
    keys = set()
    max_key = -1
    consecutive3 = []
    consecutive3_chr = defaultdict(list)
    while True:
        h = md5(salt + str(i))

        while consecutive3 and i - consecutive3[0][0] > 1000:
            (j, c) = consecutive3[0]
            consecutive3 = consecutive3[1:]
            consecutive3_chr[c] = consecutive3_chr[c][1:]

        for c in consecutive(h, 5):
            for j in consecutive3_chr[c]:
                keys |= {j}
                max_key = max(max_key, j)
                
        cs = consecutive(h, 3)
        if cs:
            consecutive3 += [(i, cs[0])]
            consecutive3_chr[cs[0]] += [i]

        if len(keys) >= 64 and max_key < i - 1000:
            break

        i += 1

    return sorted(list(keys))[63]


def consecutive(s, n):
    count = 0
    p = chr(ord(s[0]) + 1)
    r = []
    for c in s:
        if c != p:
            count = 0
        p = c
        count += 1
        if count == n:
            r += [c]
    return r


def md5(v):
    m = hashlib.md5()
    m.update(v.encode('utf-8'))
    return m.hexdigest()


salt = input().strip()
print(step1(salt))
