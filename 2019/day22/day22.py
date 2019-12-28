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


def step1(inp):
    deck = list(range(0, 10007))
    shuffle(inp, deck)
    for i, el in enumerate(deck):
        if el == 2019:
            return i


inp = list(map(str.strip, sys.stdin.readlines()))
print(step1(inp))
