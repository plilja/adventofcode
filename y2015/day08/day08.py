import re
import sys


def step1(lines):
    escs = [re.compile('\\\\\\\\'), re.compile('\\\\x[0-9a-f][0-9a-f]'), re.compile('\\\\"')]
    ans = 0
    for s in map(str.strip, lines):
        ans += len(s)
        escaped = s[1:-1]
        for esc in escs:
            escaped = esc.sub('_', escaped)
        ans -= len(escaped)
    return ans


def step2(lines):
    escs = ['"', "\\"]
    ans = 0
    for s in map(str.strip, lines):
        ans += len(s)
        for esc in escs:
            s = s.replace(esc, '_' + esc)
        ans -= len(s) + 2
    return -ans


def main():
    lines = sys.stdin.readlines()
    print(step1(lines))
    print(step2(lines))


if __name__ == '__main__':
    main()
