M = ord('z') - ord('a') + 1


def next_passwd(p):
    def is_valid(p):
        invalid = {'i', 'o', 'l'}
        if len(set(p) & invalid) > 0:
            return False

        pairs = set()
        for i in range(0, len(p) - 1):
            if p[i] == p[i + 1] and i - 1 not in pairs:
                pairs |= {i}
        if len(pairs) < 2:
            return False

        straight = False
        for i in range(0, len(p) - 2):
            if ord(p[i]) + 1 == ord(p[i + 1]) and ord(p[i + 1]) + 1 == ord(p[i + 2]):
                straight = True
        if not straight:
            return False

        return True

    def inc(p):
        c = p[-1]
        if c == 'z':
            return inc(p[:-1]) + 'a'
        else:
            return p[:-1] + chr(ord(c) + 1)

    while True:
        p = inc(p)
        if is_valid(p):
            return p


def main():
    step1 = next_passwd(input())
    print(step1)
    step2 = next_passwd(step1)
    print(step2)


if __name__ == '__main__':
    main()
