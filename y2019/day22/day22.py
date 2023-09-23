import sys
import re


def get_num(s):
    return int(re.findall(r'-?\d+', s)[0])


def deal_with_increment(deck, n):
    new_deck = [-1] * len(deck)
    i = 0
    j = 0
    while j < len(deck):
        new_deck[i] = deck[j]
        i = (i + n) % len(deck)
        j += 1
    for k in range(0, len(deck)):
        deck[k] = new_deck[k]


def cut(deck, n):
    if n < 0:
        cut(deck, len(deck) + n)
    else:
        new_deck = deck[n:] + deck[:n]
        for i in range(0, len(deck)):
            deck[i] = new_deck[i]


def deal_into_new_stack(deck):
    deck.reverse()


def shuffle(shuffles, deck):
    for shuffle in shuffles:
        if shuffle.startswith('deal with increment'):
            n = get_num(shuffle)
            deal_with_increment(deck, n)
        elif shuffle.startswith('cut'):
            n = get_num(shuffle)
            cut(deck, n)
        else:
            deal_into_new_stack(deck)
            assert shuffle == 'deal into new stack'
    return deck


def step1(shuffles):
    deck = list(range(0, 10007))
    shuffle(shuffles, deck)
    for i, el in enumerate(deck):
        if el == 2019:
            return i


def ext_gcd(a, b):
    s = 0
    t = 1
    r = b
    old_s = 1
    old_t = 0
    old_r = a
    while r != 0:
        q = old_r // r

        tmp1 = r
        r = old_r - q * r
        old_r = tmp1

        tmp2 = s
        s = old_s - q * s
        old_s = tmp2

        tmp3 = t
        t = old_t - q * t
        old_t = tmp3
    return (old_s, old_t, old_r)


def geometric_sum(a, e, p):
    if e == 0:
        return 1
    elif e % 2 == 1:
        t = geometric_sum(a * a % p, e // 2, p)
        return (t + a * t) % p
    else:
        t = geometric_sum(a, e - 1, p)
        return (1 + a * t) % p


def mod_pow(x, e, p):
    if e < 2:
        return (x**e) % p
    else:
        e2 = e // 2
        t = mod_pow(x, e2, p)
        r = t * t % p
        if e % 2 != 0:
            r = (r * x) % p
        return r


def step2(shuffles):
    loops = 101741582076661
    size = 119315717514047
    equation = [1, 0]
    for shuff in reversed(shuffles):
        if shuff.startswith('deal with increment'):
            n = get_num(shuff)
            a, b, g = ext_gcd(n, size)
            equation[0] *= a
            equation[1] *= a
        elif shuff.startswith('cut'):
            n = get_num(shuff)
            if n < 0:
                n = (size + n) % size
            equation[1] += n
        else:
            assert shuff == 'deal into new stack'
            equation[0] *= -1
            equation[1] = -equation[1] - 1

    w = 2020
    t1 = mod_pow(equation[0], loops, size) * w
    t2 = equation[1] * geometric_sum(equation[0], loops - 1, size)
    return (t1 + t2) % size


inp = list(map(str.strip, sys.stdin.readlines()))
print(step1(inp))
print(step2(inp))
