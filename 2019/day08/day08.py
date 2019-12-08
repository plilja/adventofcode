def step1(inp):
    w = 25
    h = 6
    size = w * h
    minimum = float('inf')
    res = None
    for i in range(0, len(inp) // size):
        layer = inp[i * size:(i + 1) * size]
        zeros = len(list(filter(lambda x: x == '0', layer)))
        if zeros < minimum:
            minimum = zeros
            ones = len(list(filter(lambda x: x == '1', layer)))
            twos = len(list(filter(lambda x: x == '2', layer)))
            res = ones * twos
    return res


inp = input()
print(step1(inp))
