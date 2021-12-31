import sys


def step1(scanners):
    correctly_rotated = {0}
    tested = set()
    while len(correctly_rotated) < len(scanners):
        for i in range(0, len(scanners)):
            scanner1 = scanners[i]
            if i not in correctly_rotated:
                continue
            for j in range(0, len(scanners)):
                if j in correctly_rotated or (i, j) in tested:
                    continue
                scanner2 = scanners[j]
                tested |= {(i, j)}
                correct_rotation = find_rotation(scanner1, scanner2)
                if correct_rotation:
                    scanners[j] = correct_rotation
                    correctly_rotated.add(j)
    result = set()
    for scanner in scanners:
        for beacon in scanner:
            result.add(beacon)
    return len(result)


def find_rotation(scanner1, scanner2):
    beacons1 = set(scanner1)
    for rot in rotations(scanner2):
        for x1, y1, z1 in scanner1[11:]:
            for x2, y2, z2 in rot:
                dx = x1 - x2
                dy = y1 - y2
                dz = z1 - z2
                rem = len(rot)
                matches = 0
                for x3, y3, z3 in rot:
                    beacon = (x3 + dx, y3 + dy, z3 + dz)
                    if beacon in beacons1:
                        matches += 1
                    rem -= 1
                    if rem + matches < 12:
                        break
                if matches >= 12:
                    ls = []
                    for x3, y3, z3 in rot:
                        ls.append((x3 + dx, y3 + dy, z3 + dz))
                    return ls
    return None


def rotations(scanner):
    perms = [
             ((0, 1), (1, 1), (2, 1)),
             ((1, 1), (2, 1), (0, 1)),
             ((0, -1), (2, 1), (1, 1)),
             ((2, 1), (0, -1), (1, -1)),
             ((2, 1), (1, 1), (0, -1)),
             ((0, 1), (1, -1), (2, -1))]
    result = []
    for (a, da), (b, db), (c, dc) in perms:
        result.append([])
        for beacon in scanner:
            ls = [0, 0, 0]
            ls[0] = beacon[a] * da
            ls[1] = beacon[b] * db
            ls[2] = beacon[c] * dc
            result[-1].append(tuple(ls))
        for j in range(0, 3):
            result.append([])
            for x, y, z in result[-2]:
                result[-1].append((y, -x, z))
    assert len(result) == 24
    return result


def read_input():
    scanners = []
    for line in sys.stdin:
        if 'scanner' in line:
            scanners.append([])
        elif line.strip():
            [x, y, z] = list(map(int, line.split(',')))
            scanners[-1].append((x, y, z))
    return scanners


scanners = read_input()
print(step1(scanners))
