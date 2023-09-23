import sys

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

SCORE = {ROCK: 1,
         PAPER: 2,
         SCISSORS: 3
         }

WIN = {ROCK: SCISSORS,
       PAPER: ROCK,
       SCISSORS: PAPER
       }

LOSE = {SCISSORS: ROCK,
        PAPER: SCISSORS,
        ROCK: PAPER
        }

SYMBOLS = {'A': ROCK,
           'B': PAPER,
           'C': SCISSORS
           }


def score(opponent, you):
    result = 0
    if opponent != you:
        if WIN[you] == opponent:
            result += 6
    else:
        # draw
        result += 3
    return result + SCORE[you]


def step1(inp):
    symbols2 = {'X': ROCK,
                'Y': PAPER,
                'Z': SCISSORS
                }
    result = 0
    for a, b in inp:
        result += score(SYMBOLS[a], symbols2[b])
    return result


def step2(inp):
    result = 0
    for a, b in inp:
        opp = SYMBOLS[a]
        if b == 'X':
            you = WIN[opp]
        elif b == 'Y':
            you = opp
        else:
            you = LOSE[opp]
        result += score(opp, you)
    return result


def read_input():
    result = []
    for line in sys.stdin:
        a, b = line.strip().split(' ')
        result.append((a, b))
    return result


def main():
    inp = read_input()
    print(step1(inp))
    print(step2(inp))


if __name__ == '__main__':
    main()
