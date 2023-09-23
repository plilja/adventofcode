import sys
from collections import deque, Counter


def step1(nums):
    q = deque()
    counter = Counter()
    for i, num in enumerate(nums):
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


def step2(nums):
    weakness = step1(nums)
    acc = 0
    starts = {}
    for i, num in enumerate(nums):
        starts[acc] = i
        acc += num
        rem = acc - weakness
        if rem in starts:
            start = starts[rem]
            seq = nums[start:i + 1]
            return min(seq) + max(seq)
    raise ValueError('Unable to find solution')


def main():
    nums = [int(x) for x in sys.stdin]
    print(step1(nums))
    print(step2(nums))


if __name__ == '__main__':
    main()
