import hashlib
import sys


def md5(v):
    m = hashlib.md5()
    m.update(v.encode('utf-8'))
    return m.hexdigest()


def solve(n, input):
    for inp in input:
        i = 0
        while True:
            if md5(inp + str(i))[:n] == (n * '0'):
                break
            else:
                i += 1
        print(i)

n = int(sys.argv[1])
solve(n, map(str.strip, sys.stdin.readlines()))
