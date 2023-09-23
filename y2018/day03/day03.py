import sys
import re
from collections import namedtuple, defaultdict

Claim = namedtuple('Claim', 'id left top width height')


def claim_points(claim):
    for y in range(0, claim.height):
        for x in range(0, claim.width):
            yield x, y


def step1(claims):
    d = defaultdict(lambda: defaultdict(int))
    r = 0
    for claim in claims:
        for x, y in claim_points(claim):
            c = d[claim.top + y][claim.left + x]
            d[claim.top + y][claim.left + x] += 1
            if c == 1:
                r += 1
    return r


def step2(claims):
    d = defaultdict(lambda: defaultdict(set))
    for claim in claims:
        for x, y in claim_points(claim):
            d[claim.top + y][claim.left + x] |= {claim.id}
    for claim in claims:
        poss = True
        for x, y in claim_points(claim):
            if d[claim.top + y][claim.left + x] != {claim.id}:
                poss = False
                break
        if poss:
            return claim.id
    raise ValueError('No solution found')


def read_claims():
    claims = []
    for line in sys.stdin:
        claim_id, left, right, width, height = re.match(
            r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)',
            line
        ).groups()
        claims += [Claim(int(claim_id), int(left),
                         int(right), int(width), int(height))]
    return claims


def main():
    claims = read_claims()
    print(step1(claims))
    print(step2(claims))


if __name__ == '__main__':
    main()
