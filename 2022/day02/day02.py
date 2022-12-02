import sys

ROCK = 1
PAPER = 2
SCISSORS = 3

SCORE = {'X': 1,
         'Y': 2,
         'Z': 3
         }

SYMBOLS = {'X': ROCK,
           'Y': PAPER,
           'Z': SCISSORS,
           'A': ROCK,
           'B': PAPER,
           'C': SCISSORS
           }


WIN = {ROCK: SCISSORS,
       PAPER: ROCK,
       SCISSORS: PAPER
       }


def score(opponent, you):
    a = SYMBOLS[opponent]
    b = SYMBOLS[you]
    result = 0
    if a != b:
        if WIN[b] == a:
            result += 6
    else:
        # draw
        result += 3
    return result + SCORE[you]


def step1(inp):
    result = 0
    for opp, you in inp:
        result += score(opp, you)
    return result


def read_input():
    result = []
    for line in sys.stdin:
        a, b = line.strip().split(' ')
        result.append((a, b))
    return result


inp = read_input()
print(step1(inp))
