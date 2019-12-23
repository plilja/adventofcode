BASE_PATTERN = [0, 1, 0, -1]


def step1(signal):
    r = [int(t) for t in signal]
    for phase in range(0, 100):
        next_r = []
        for out in range(1, len(signal) + 1):
            acc = 0
            for i in range(0, len(signal)):
                t = (i + 1) // out % len(BASE_PATTERN)
                x = r[i] * BASE_PATTERN[t]
                acc += x
            next_r.append(abs(acc) % 10)
        r = next_r
    return ''.join(list(map(str, r)))[0:8]


signal = input()
print(step1(signal))
