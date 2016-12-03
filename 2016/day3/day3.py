import sys

r = 0
for line in sys.stdin.readlines():
    [a, b, c] = sorted(map(int, line.strip().split()))
    if a + b > c:
        r += 1

print(r)
