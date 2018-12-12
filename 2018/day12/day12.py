import sys
from collections import defaultdict

def step1(initial_state, notes):
    assert '......' not in notes
    state = defaultdict(lambda: '.')
    min_pot = 0
    max_pot = len(initial_state)
    for i in range(0, len(initial_state)):
        state[i] = initial_state[i]
    for i in range(0, 20):
        next_state = defaultdict(lambda: '.')
        for j in range(min_pot - 2, max_pot + 3):
            key = ''.join([state[j + k] for k in range(-2, 3)])
            next_state[j] = notes.get(key, '.')
        state = next_state
        for k in state.keys():
            if state[k] == '#':
                min_pot = min(min_pot, k)
                max_pot = max(max_pot, k)
    return sum([k for k in state.keys() if state[k] == '#'])


state = input().split()[2]
input() # skip blank row
notes = {k:v for k, _, v in map(str.split, sys.stdin.readlines())}
print(step1(state, notes))
