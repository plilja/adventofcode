import hashlib
from queue import PriorityQueue


def step1(passcode):
    def open(c):
        return c >= 'b' and c <= 'f'

    pq = PriorityQueue()
    pq.put((0, 0, 0, passcode))
    while not pq.empty():
        (dist, x, y, path) = pq.get()
        if x == 3 and y == 3:
            return path[len(passcode):]

        h = md5(path)
        if y > 0 and open(h[0]):
            pq.put((dist + 1, x, y - 1, path + 'U'))
        if y < 3 and open(h[1]):
            pq.put((dist + 1, x, y + 1, path + 'D'))
        if x > 0 and open(h[2]):
            pq.put((dist + 1, x - 1, y, path + 'L'))
        if x < 3 and open(h[3]):
            pq.put((dist + 1, x + 1, y, path + 'R'))

    return 'IMPOSSIBLE'


def md5(v):
    m = hashlib.md5()
    m.update(v.encode('utf-8'))
    return m.hexdigest()


passcode = input()
print(step1(passcode))
