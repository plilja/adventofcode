import sys
from collections import defaultdict


def step1(draw, boards):
    num_to_board = defaultdict(list)
    for board_num, board in enumerate(boards):
        for y in range(0, 5):
            for x in range(0, 5):
                num_to_board[board[y][x]].append((board_num, x, y))
    bingo = [defaultdict(lambda: defaultdict(int)) for i in range(0, len(boards))]
    for num in draw:
        for board_num, x, y in num_to_board[num]:
            bingo[board_num][y][x] = 1
        for board_num, board in enumerate(boards):
            is_bingo = False
            for a in range(0, 5):
                s1 = sum(map(lambda b: bingo[board_num][a][b], range(0, 5)))
                s2 = sum(map(lambda b: bingo[board_num][b][a], range(0, 5)))
                is_bingo = is_bingo or s1 == 5
                is_bingo = is_bingo or s2 == 5

            if is_bingo:
                result = 0
                for y in range(0, 5):
                    for x in range(0, 5):
                        if bingo[board_num][y][x] == 0:
                            result += board[y][x]
                return result * num
    raise ValueError('No bingo')


def read_input():
    lines = sys.stdin.readlines()
    draw = [int(i) for i in lines[0].split(',')]
    boards = []
    for i in range(1, len(lines), 6):
        boards.append([])
        for j in range(1, 6):
            boards[-1].append(list(map(int, lines[i + j].split())))
    return draw, boards


draw, boards = read_input()
print(step1(draw, boards))
