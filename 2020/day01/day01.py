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


def step2(nums):
    counts = Counter(nums)
    for num1 in sorted(counts.keys()):
        for num2 in sorted(counts.keys()):
            if num2 > num1:
                break
            if num1 == num2 and counts[num1] < 2:
                continue
            rem = 2020 - num1 - num2
            if num1 == num2 and num2 == rem and counts[rem] >= 3:
                return num1 * num2 * rem
            elif num1 == rem or num2 == rem and counts[rem] >= 2:
                return num1 * num2 * rem
            elif counts[rem] >= 1:
                return num1 * num2 * rem
    raise ValueError('Unable to find solution')


nums = list(map(int, sys.stdin.readlines()))
print(step1(nums))
print(step2(nums))
