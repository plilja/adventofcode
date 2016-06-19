import hashlib
import sys


def md5(v):
    m = hashlib.md5()
    m.update(v.encode('utf-8'))
    return m.hexdigest()


for inp in map(str.strip, sys.stdin.readlines()):
    i = 0
    while True:
        if md5(inp + str(i))[:5] == '00000':
            break
        else:
            i += 1
    print(i)
