import sys


def step1(start, ops):
    passwd = [x for x in start]
    for op in ops:
        parts = op.split()
        if parts[0] == 'swap' and parts[1] == 'position':
            x = int(parts[2])
            y = int(parts[5])
            passwd[x], passwd[y] = passwd[y], passwd[x]
        elif parts[0] == 'reverse':
            x = min(int(parts[2]), int(parts[4]))
            y = max(int(parts[2]), int(parts[4]))
            for i in range(0, (y - x + 1) // 2):
                passwd[x + i], passwd[y - i] = passwd[y - i], passwd[x + i]
        elif parts[0] == 'swap' and parts[1] == 'letter':
            x = parts[2][0]
            y = parts[5][0]
            for i in range(0, len(passwd)):
                if passwd[i] == x:
                    passwd[i] = y
                elif passwd[i] == y:
                    passwd[i] = x
        elif parts[0] == 'rotate':
            if parts[1] == 'based':
                x = passwd.index(parts[6][0])
                i = x
                if x >= 4:
                    x += 1
                x += 1
                direction = 'right'
            else:
                x = int(parts[2])
                direction = parts[1]
            x = x % len(passwd)
            if direction == 'left':
                passwd = passwd[x:] + passwd[:x]
            else:
                passwd = passwd[-x:] + passwd[:-x]
        else:
            assert parts[0] == 'move'
            x = int(parts[2])
            y = int(parts[5])
            tmp = passwd[x]
            passwd = passwd[:x] + passwd[x + 1:]
            passwd = passwd[:y] + [tmp] + passwd[y:]

    return ''.join(passwd)



start = input()
ops = sys.stdin.readlines()
print(step1(start, ops))
