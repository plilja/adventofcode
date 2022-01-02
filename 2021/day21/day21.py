def step1(player1, player2):
    dice_rolls = 0
    next_roll = 1
    players = [player1, player2]
    scores = [0, 0]
    while max(scores) < 1000:
        for i in range(0, len(players)):
            total = 0
            for j in range(0, 3):
                total += next_roll
                dice_rolls += 1
                next_roll += 1
            players[i] = (((players[i] - 1) + total) % 10) + 1
            scores[i] += players[i]
            if scores[i] >= 1000:
                break
    return min(scores) * dice_rolls


player1 = int(input().split()[-1])
player2 = int(input().split()[-1])
print(step1(player1, player2))
