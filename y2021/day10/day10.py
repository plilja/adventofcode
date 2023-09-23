import sys

CLOSING = {'(': ')', '[': ']', '{': '}', '<': '>'}


def step1(inp):
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    result = 0
    for line in inp:
        stack = []
        for c in line:
            if c in CLOSING:
                stack.append(CLOSING[c])
            elif c in CLOSING.values():
                if not stack or stack[-1] != c:
                    result += scores[c]
                    break
                else:
                    stack.pop()
            else:
                raise ValueError('Illegal character %s encountered' % c)
    return result


def step2(inp):
    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    rows = []
    for line in inp:
        valid = True
        stack = []
        for c in line:
            if c in CLOSING:
                stack.append(CLOSING[c])
            elif c in CLOSING.values():
                if not stack or stack[-1] != c:
                    valid = False
                    break  # Illegal, discard row
                else:
                    stack.pop()
            else:
                raise ValueError('Illegal character %s encountered' % c)
        if valid:
            score = 0
            for c in stack[::-1]:
                score = 5 * score + scores[c]
            rows.append(score)

    rows.sort()
    return rows[len(rows) // 2]


def main():
    inp = [s.strip() for s in sys.stdin]
    print(step1(inp))
    print(step2(inp))


if __name__ == '__main__':
    main()
