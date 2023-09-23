from collections import Counter


def step1(datastream):
    return solve(datastream, 4)


def step2(datastream):
    return solve(datastream, 14)


def solve(datastream, count):
    counter = Counter()
    for i in range(0, len(datastream)):
        counter[datastream[i]] += 1
        if i >= count:
            c = datastream[i - count]
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]
        if i >= count - 1 and len(counter) == count:
            return i + 1
    return -1


datastream = input()
print(step1(datastream))
print(step2(datastream))
