from collections import Counter


def step1(datastream):
    counter = Counter()
    for i in range(0, len(datastream)):
        counter[datastream[i]] += 1
        if i >= 4:
            c = datastream[i - 4]
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]
        if i >= 3 and len(counter) == 4:
            return i + 1
    return -1


datastream = input()
print(step1(datastream))
