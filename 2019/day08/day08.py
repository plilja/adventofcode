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


def step2(inp):
    w = 25
    h = 6
    pixel_map = {'0': ' ', '1': '*', '2': '-'}
    image = [['-'] * w for _ in range(0, h)]
    size = w * h
    for i in range(0, len(inp) // size):
        layer = inp[i * size:(i + 1) * size]
        for y in range(0, h):
            for x in range(0, w):
                image_pixel = image[y][x]
                if image_pixel == '-':
                    image[y][x] = pixel_map[layer[y * w + x]]
    return '\n'.join([''.join(x) for x in image])


inp = input()
print(step1(inp))
print(step2(inp))
