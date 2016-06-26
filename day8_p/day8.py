import sys
import re

escs = [re.compile('\\\\\\\\'), re.compile('\\\\x[0-9a-f][0-9a-f]'), re.compile('\\\\"')]

ans = 0
for s in map(str.strip, sys.stdin.readlines()):
    ans += len(s)
    escaped = s[1:-1]
    for esc in escs:
        escaped = esc.sub('_', escaped)
    ans -= len(escaped)

print(ans)
