import sys


def read_input():
    ings = []
    for s in sys.stdin.readlines():
        s = s.replace(',', '')
        [ing, _, capacity, _, durability, _, flavor, _, texture, _, calories] = s.split()
        ings += [list(map(int, [capacity, durability, flavor, texture, calories]))]
    return ings


def solve(ings, pred):
    def f(ings, rem, recipe=[]):
        if not ings:
            res = [0, 0, 0, 0, 0]
            for r in recipe:
                for i in range(0, len(res)):
                    res[i] += r[i]
            for i in res:
                if i < 0:
                    return 0
            a = 1
            for i in res[:-1]:
                a *= i
            if pred(res[-1]):
                return a
            else:
                return -1

        best = 0
        if len(ings) == 1:
            poss = [rem]
        else:
            poss = range(0, rem + 1)
        for i in poss:
            tmp = list(map(lambda x: i * x, ings[0]))
            best = max(best, f(ings[1:], rem - i, recipe + [tmp]))
        return best

    return f(ings, 100, )


ings = read_input()
print(solve(ings, lambda calories: True))
print(solve(ings, lambda calories: calories == 500))
