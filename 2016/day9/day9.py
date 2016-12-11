import re
import sys

p = re.compile('\(\d+x\d+\)')

def step1(inp):
    def decompress(s):
        m = p.search(s)
        if not m:
            return len(s)
        else:
            i = m.start()
            j = m.end()
            marker = s[i+1:j-1]
            [chars, repeat] = list(map(int, marker.split('x')))
            return i + chars * repeat + decompress(s[j + chars:])

    return sum([decompress(s) for s in inp])

inp = list(map(str.strip, sys.stdin.readlines()))
print(step1(inp))
