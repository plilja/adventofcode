import sys
from collections import *
import re

Claim = namedtuple('Claim', 'id left top width height')

def step1(claims):
    d = defaultdict(lambda: defaultdict(int))
    r = 0
    for claim in claims:
        for y in range(0, claim.height):
            for x in range(0, claim.width):
                c = d[claim.top + y][claim.left + x]
                d[claim.top + y][claim.left + x] += 1
                if c == 1:
                    r += 1
    return r
    

def read_claims():
    claims = []
    for line in sys.stdin:
        claim_id, left, right, width, height = re.match(
                r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', 
                line
                ).groups()
        claims += [Claim(int(claim_id), int(left), int(right), int(width), int(height))]
    return claims


claims = read_claims()
print(step1(claims))
