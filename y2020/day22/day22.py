import sys
from collections import deque


def score(deck):
    score = 0
    i = 1
    while deck:
        x = deck.pop()
        score += i * x
        i += 1
    return score


def step1(inp):
    players = [deque(inp[0]), deque(inp[1])]
    while players[0] and players[1]:
        i = 0 if players[0] > players[1] else 1
        card0 = players[i].popleft()
        players[i].append(card0)
        card1 = players[(i + 1) % 2].popleft()
        players[i].append(card1)

    winner = 0 if len(players[1]) == 0 else 1
    return score(players[winner])


def step2(inp):
    def play(players, seen):
        while players[0] and players[1]:
            if any(filter(lambda x: tuple(x) in seen, players)):
                return 0  # loop detected, player 0 wins (problem desc, is 1 indexed
            for player in players:
                seen.add(tuple(player))
            card0 = players[0].popleft()
            card1 = players[1].popleft()
            if card0 <= len(players[0]) and card1 <= len(players[1]):
                new_stack1 = deque(list(players[0])[:card0])
                new_stack2 = deque(list(players[1])[:card1])
                round_winner = play([new_stack1, new_stack2], set())
            else:
                round_winner = 0 if card0 > card1 else 1
            players[round_winner].append(card0 if round_winner == 0 else card1)
            players[round_winner].append(card1 if round_winner == 0 else card0)
        return 0 if players[0] else 1

    players = [deque(inp[0]), deque(inp[1])]
    winner = play(players, set())
    return score(players[winner])


def read_input():
    result = []
    for line in sys.stdin:
        if line.startswith('Player'):
            result.append([])
        elif line.strip() != '':
            result[-1].append(int(line))
    return result[0], result[1]


inp = read_input()
print(step1(inp))
print(step2(inp))
