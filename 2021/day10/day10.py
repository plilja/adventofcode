import sys

SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
CLOSING = {'(': ')', '[': ']', '{': '}', '<': '>'}


def step1(inp):
    result = 0
    stack = []
    for line in inp:
        for c in line:
            if c in CLOSING:
                stack.append(CLOSING[c])
            elif c in CLOSING.values():
                if stack[-1] != c:
                    result += SCORES[c]
                    break
                else:
                    stack.pop()
            else:
                raise ValueError('Illegal character %s encountered' % c)
    return result


inp = [s.strip() for s in sys.stdin]
print(step1(inp))
