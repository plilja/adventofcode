import sys
from math import *

winner_dist = 0

TIME = 2503

for i in sys.stdin.readlines():
    [reindeer, can, fly, speed, unit, _for1, num1, seconds1, 
            but, then, must, rest, _for2, num2, seconds2] = i.split()
    [speed, num1, num2] = list(map(int, [speed, num1, num2]))
    cycles = floor(TIME / (num1 + num2))
    rem = min(num1, TIME - cycles * (num1 + num2))
    time_travelling = cycles * num1 + rem
    dist = speed * time_travelling
    if dist > winner_dist:
        winner_dist = dist

print(winner_dist)
