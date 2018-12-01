import sys

def step1(rows):
    return sum(map(int, rows))

print(step1(sys.stdin.readlines()))
