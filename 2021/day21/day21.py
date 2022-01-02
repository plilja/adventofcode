def step1(player1, player2):
    dice_rolls = 0
    next_roll = 1
    players = [player1, player2]
    scores = [0, 0]
    while True:
        for i in range(0, len(players)):
            total = 0
            for j in range(0, 3):
                total += next_roll
                dice_rolls += 1
                next_roll += 1
            players[i] = (((players[i] - 1) + total) % 10) + 1
            scores[i] += players[i]
            if scores[i] >= 1000:
                return min(scores) * dice_rolls


def step2(player1, player2):
    def helper(scores, positions, turn, roll, cache):
        key = (turn, roll, scores, positions)
        if key in cache:
            return cache[key]
        if roll > 3:
            new_scores = replace(scores, turn, scores[turn] + positions[turn])
            if new_scores[turn] >= 21:
                return replace((0, 0), turn, 1)
            else:
                return helper(new_scores, positions, (turn + 1) % 2, 1, cache)
        else:
            p1, p2 = 0, 0
            for k in range(1, 4):
                new_positions = replace(positions, turn, ((positions[turn] - 1 + k) % 10) + 1)
                a, b = helper(scores, new_positions, turn, roll + 1, cache)
                p1 += a
                p2 += b
            cache[key] = (p1, p2)
            return (p1, p2)
    cache = {}
    a, b = helper((0, 0), (player1, player2), 0, 1, cache)
    return max(a, b)


def replace(t, i, v):
    result = list(t)
    result[i] = v
    return tuple(result)


player1 = int(input().split()[-1])
player2 = int(input().split()[-1])
print(step1(player1, player2))
print(step2(player1, player2))
