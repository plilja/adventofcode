from collections import deque

def solve(num_players, last_marble):
    assert(last_marble >= 3)
    players = [0] * num_players
    circle = deque([0, 2, 1])
    current_player = 2
    # Always keep current marble one left of rightmost marble in circle
    for marble in range(3, last_marble + 1):
        if marble % 23 == 0:
            for _ in range(0, 8):
                circle.appendleft(circle.pop())
            players[current_player] += circle.pop()
            players[current_player] += marble
            for _ in range(0, 2):
                circle.append(circle.popleft())
        else:
            circle.append(marble)
            circle.append(circle.popleft())
        current_player = (current_player + 1) % num_players
    return max(players)


def step1(num_players, last_marble):
    return solve(num_players, last_marble)


def step2(num_players, last_marble):
    return solve(num_players, 100 * last_marble)


inp = input().split()
num_players, last_marble = int(inp[0]), int(inp[6])
print(step1(num_players, last_marble))
print(step2(num_players, last_marble))
