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


def step2(inp_signal):
    offset = int(inp_signal[0:7])
    r = list(map(int, reversed((inp_signal * 10000)[offset:])))
    # The utilizes the fact that the offset is large and ends 
    # up being in the portion of the signal where every number is
    # always multiplied by -1 (or 1 if you only consider the positive
    # numbers). This solution wouldn't work if the offset was smaller.
    for phase in range(0, 100):
        acc = 0
        next_r = []
        for i in range(0, len(r)):
            acc = (acc + r[i]) % 10
            next_r.append(acc)
        r = next_r
    r = reversed(r[-8:])
    return ''.join(list(map(str, r)))


def main():
    signal = input()
    print(step1(signal))
    print(step2(signal))


if __name__ == '__main__':
    main()
