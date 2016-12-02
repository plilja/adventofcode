import sys

keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

x, y = 1, 1

code = ''

for line in map(str.strip, sys.stdin.readlines()):
    for c in line:
        if c == 'U':
            y = max(0, y - 1)
        elif c == 'D':
            y = min(2, y + 1)
        elif c == 'L':
            x = max(0, x - 1)
        elif c == 'R':
            x = min(2, x + 1)
        else:
            raise ValueError('Illegal direction ' + c)
    code += str(keypad[y][x])

print(code)
