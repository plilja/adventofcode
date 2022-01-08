def ever(n=0):
    i = n
    while True:
        yield i
        i += 1


def neighbors4(x, y):
    return ((x + 1, y),
            (x, y - 1),
            (x - 1, y),
            (x, y + 1))


def neighbors8(x, y):
    return ((x + 1, y),
            (x + 1, y - 1),
            (x, y - 1),
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1))


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def traced(f):
    def traced_f(*args):
        result = f(*args)
        print('{}({}) = {}'.format(f.__name__, ', '.join(map(str, args)), result))
        return result

    return traced_f
