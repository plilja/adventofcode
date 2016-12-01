import sys

weapons = [('Dagger', 8, 4, 0),
            ('Shortsword', 10, 5, 0),
            ('Warhammer', 25, 6, 0),
            ('Longsword', 40, 7, 0),
            ('Greataxe', 74, 8, 0)]

armors = [('Leather', 13, 0, 1),
            ('Chainmail', 31, 0, 2),
            ('Splintmail', 53, 0, 3),
            ('Bandedmail', 75, 0, 4),
            ('Platemail', 102, 0, 5)]

rings =[('R1', 25, 1, 0),
        ('R2', 50, 2, 0),
        ('R3', 100, 3, 0),
        ('R4', 20, 0, 1),
        ('R5', 40, 0, 2),
        ('R6', 80, 0, 3)]

def read_boss():
    line = sys.stdin.readline
    [_, _, hp] = line().split()
    [_, damage] = line().split()
    [_, armor] = line().split()
    return (int(hp), int(damage), int(armor))

def solve(boss):
    def picks():
        def armor_picks():
            for a in armors:
                yield [a]
            yield []

        def ring_picks():
            yield []
            for r in rings:
                yield [r]
            for i in range(0, len(rings)):
                for j in range(i + 1, len(rings)):
                    yield [rings[i], rings[j]]

        for w in weapons:
            for a in armor_picks():
                for r in ring_picks():
                    yield ([w], a, r)

    def eval_attr(f, ws, as_, rs):
        ans = 0
        for w in ws:
            ans += f(w)
        for a in as_:
            ans += f(a)
        for r in rs:
            ans += f(r)
        return ans

    def cost(ws, as_, rs):
        return eval_attr(lambda x: x[1], ws, as_, rs)

    def damage(ws, as_, rs):
        return eval_attr(lambda x: x[2], ws, as_, rs)

    def defense(ws, as_, rs):
        return eval_attr(lambda x: x[3], ws, as_, rs)


    def wins(boss, ws, as_, rs):
        (bhp, ba, bd) = boss
        (hp, a, d) = 100, damage(ws, as_, rs), defense(ws, as_, rs)

        while bhp > 0 and hp > 0:
            bhp -= max(1, a - bd)
            if bhp > 0:
                hp -= max(1, ba - d)

        return hp > 0

    ans1 = float('inf')
    ans2 = -float('inf')
    for p in picks():
        c = cost(p[0], p[1], p[2])
        if wins(boss, p[0], p[1], p[2]):
            ans1 = min(ans1, c)
        else:
            ans2 = max(ans2, c)

    return (ans1, ans2)

print(solve(read_boss()))


