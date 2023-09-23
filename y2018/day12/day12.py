import sys
from collections import defaultdict


def step1(initial_state, notes):
    return solve(initial_state, notes, 20)


def step2(initial_state, notes):
    return solve(initial_state, notes, 50000000000)


def solve(initial_state, notes, iterations):
    assert '......' not in notes
    state = defaultdict(lambda: '.')
    for i, v in enumerate(initial_state):
        state[i] = v
    # Store seen plant generations in cache normalized so that the leftmost plant
    # is at index 0.
    cache = {}
    generation = 0
    # Off stores how much plants have been shifted to normalize plats at index 0
    off = 0
    while generation < iterations:
        tmp = {}
        for j in range(-2, max(state.keys()) + 3):
            key = ''.join([state.get(j + k, '.') for k in range(-2, 3)])
            tmp[j] = notes.get(key, '.')
        m = min([k for k, v in tmp.items() if v == '#'])
        off += m
        next_state = {k - m: v for k, v in tmp.items() if v == '#'}
        cache_key = tuple(next_state.keys())
        generation += 1
        if cache_key in cache:
            (prev_gen, prev_off) = cache[cache_key]
            d = generation - prev_gen
            loops = (iterations - i - 1) // d
            generation += d * loops
            off += loops * (off - prev_off)

        cache[cache_key] = (generation, off)
        state = next_state

    return sum([k + off for k in state.keys() if state[k] == '#'])


state = input().split()[2]
input()  # skip blank row
notes = {k: v for k, _, v in map(str.split, sys.stdin.readlines())}
print(step1(state, notes))
print(step2(state, notes))

