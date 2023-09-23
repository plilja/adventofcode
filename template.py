import sys
import re
import math

from collections import Counter, defaultdict, namedtuple, deque
from functools import lru_cache
from itertools import permutations, combinations, chain, cycle, product, islice
from heapq import heappop, heappush

from common.math_util import *
from common.timer import *
from common.util import *

INF = float('inf')

def step1(inp):
    pass

def read_input():
    return [line.strip() for line in sys.stdin]

inp = read_input()
print(step1(inp))