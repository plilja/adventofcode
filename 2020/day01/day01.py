import sys
from collections import Counter


def step1(nums):
    counts = Counter(nums)
    for num in counts.keys():
        rem = 2020 - num
        if num == rem and counts[rem] >= 2:
            return num * rem
        elif counts[rem] >= 1:
            return num * rem
    raise ValueError('Unable to find solution')


nums = list(map(int, sys.stdin.readlines()))
print(step1(nums))
