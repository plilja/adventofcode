import sys
from collections import deque, Counter


def step1(nums):
    q = deque()
    counter = Counter()
    for i in range(0, len(nums)):
        num = nums[i]
        if i >= 25:
            good = False
            for x in q:
                rem = num - x
                if rem == num:
                    if counter[rem] == 2:
                        good = True
                        break
                else:
                    if counter[rem] == 1:
                        good = True
                        break
            if not good:
                return num
            r = q.popleft()
            counter[r] -= 1
        q.append(num)
        counter[nums[i]] += 1


nums = [int(x) for x in sys.stdin]
print(step1(nums))
