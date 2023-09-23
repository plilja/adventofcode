import sys
from collections import namedtuple, defaultdict
from math import sqrt


TileRotation = namedtuple('TileRotation', 'id top right bottom left edges pattern')
Tile = namedtuple('Tile', 'id rotations')

SEA_MONSTER = ['..................#.',
               '#....##....##....###',
               '.#..#..#..#..#..#...']

DELTAS = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0),
        ]


def solve_helper(matrix, side, tiles, side_to_tiles, remaining_tiles, min_x, max_x, min_y, max_y):
    assert max_x - min_x <= side
    assert max_y - min_y <= side
    if not remaining_tiles:
        return True
    best = None
    best_x, best_y = None, None
    for x, y in frozenset(matrix.keys()):
        if matrix[(x, y)] is None:
            continue

        for dx, dy in DELTAS:
            if max(max_x, x + dx) - min(min_x, x + dx) >= side:
                continue
            if max(max_y, y + dy) - min(min_y, y + dy) >= side:
                continue
            if matrix[(x + dx, y + dy)] is None:
                key = [-1] * 4
                for i, (dx2, dy2) in enumerate(DELTAS):
                    tile = matrix[(x + dx + dx2, y + dy + dy2)]
                    if tile is not None:
                        key[i] = tile.edges[(i + 2) % 4]
                assert key != [-1] * 4
                candidate = side_to_tiles[tuple(key)]
                remove = set()
                for c in candidate:
                    if c.id not in remaining_tiles:
                        remove.add(c)
                candidate = candidate - remove
                if min_x <= x + dx <= max_x and min_y <= y + dy <= max_y and not candidate:
                    return False
                if candidate:
                    if best is None or len(best) > len(candidate):
                        best = candidate
                        best_x, best_y = x + dx, y + dy
    for tile in best:
        matrix[(best_x, best_y)] = tile
        if solve_helper(matrix,
                        side,
                        tiles,
                        side_to_tiles,
                        remaining_tiles - {tile.id},
                        min(min_x, best_x),
                        max(max_x, best_x),
                        min(min_y, best_y),
                        max(max_y, best_y)):
            return True
        matrix[(best_x, best_y)] = None
    return False


def solve(tiles):
    side = int(sqrt(len(tiles)))
    side_to_tiles = defaultdict(set)
    for tile in tiles.values():
        for r in tile.rotations:
            for i in range(0, 16):
                b = ('0000' + bin(i)[2:])[-4:]
                key = [-1] * 4
                for j in range(0, 4):
                    if b[j] == '1':
                        key[j] = r.edges[j]
                side_to_tiles[tuple(key)].add(r)

    matrix = defaultdict(lambda: None)
    any_tile = list(tiles.values())[0]
    matrix[(0, 0)] = any_tile.rotations[0]
    t = solve_helper(matrix, side, tiles, side_to_tiles, frozenset(tiles.keys()) - {any_tile.id}, 0, 0, 0, 0)
    assert t
    min_x, max_x, min_y, max_y = float('INF'), -float('INF'), float('INF'), -float('INF')
    for x, y in matrix.keys():
        if matrix[(x, y)] is None:
            continue
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        min_y = min(y, min_y)
        max_y = max(y, max_y)
    result = [[None] * side for foo in range(0, side)]
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            result[y - min_y][x - min_x] = matrix[(x, y)]
    return result


def step1(tiles):
    matrix = solve(tiles)
    side = len(matrix)
    return matrix[0][0].id * \
           matrix[side - 1][0].id * \
           matrix[0][side - 1].id * \
           matrix[side - 1][side - 1].id


def rotations(pattern):
    def rotate_once(pattern):
        x_len = len(pattern[0])
        y_len = len(pattern)
        new_pattern = [['?'] * y_len for y in range(0, x_len)]
        for y in range(0, y_len):
            for x in range(0, x_len):
                new_pattern[x][y_len - y - 1] = pattern[y][x]
        for y, row in enumerate(new_pattern):
            new_pattern[y] = tuple(row)
        return tuple(new_pattern)
    result = [rotate_once(pattern)]
    for i in range(0, 3):
        result.append(rotate_once(result[-1]))
    return tuple(result)


def transformations(pattern):
    result = rotations(pattern)
    result += rotations(list(reversed(pattern)))
    result += rotations([list(reversed(x)) for x in pattern])
    return tuple(set(result))


def matches(pattern, s):
    result = set()
    for i in range(0, len(s) - len(pattern)):
        m = True
        for j in range(0, len(pattern)):
            if pattern[j] != '.' and pattern[j] != s[i + j]:
                m = False
                break
        if m:
            result.add(i)
    return result


def step2(tiles):
    matrix = solve(tiles)
    n = len(matrix)
    m = len(tiles[matrix[0][0].id].rotations[0].top) - 2
    original_grid = ['' for x in range(0, n*m)]
    for y1 in range(0, n):
        for x1 in range(0, n):
            tilerot = matrix[y1][x1]
            for y2 in range(0, m):
                for x2 in range(0, m):
                    original_grid[y1*m + y2] = original_grid[y1*m + y2] + tilerot.pattern[y2 + 1][x2 + 1]

    brackets = sum([len(list(filter(lambda x: x == '#', row))) for row in original_grid])

    for grid in transformations(original_grid):
        result = 0
        for y, row in enumerate(grid):
            if y + len(SEA_MONSTER) >= len(grid):
                break

            s = set([i for i in range(0, len(row))])
            for i, pattern in enumerate(SEA_MONSTER):
                s &= matches(pattern, ''.join(grid[y + i]))
            if s:
                result += len(s)
        if result > 0:
            return brackets - result * 15

    raise ValueError('No solution found')


def make_tile_rotation(id_, pattern):
    top = ''.join(pattern[0])
    right = ''.join([x[-1] for x in pattern])
    bottom = ''.join(pattern[-1])
    left = ''.join([x[0] for x in pattern])
    edges = (top, right, bottom, left)
    pattern_as_tuple = tuple([tuple(x) for x in pattern])
    return TileRotation(id_, top, right, bottom, left, edges, pattern_as_tuple)



def read_input():
    def convert_to_tile(id_, pattern):
        trans = []
        for t in transformations(pattern):
            trans.append(make_tile_rotation(id_, t))
        return Tile(id_, tuple(trans))
    tiles = {}
    pattern = []
    id_ = None
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            tiles[id_] = convert_to_tile(id_, pattern)
            pattern = []
            id_ = None
        elif line.startswith('Tile '):
            id_ = int(line.replace(':', '').split(' ')[1])
        else:
            pattern.append(list(line))
    if id_:
        tiles[id_] = convert_to_tile(id_, pattern)
    return tiles


tiles = read_input()
print(step1(tiles))
print(step2(tiles))
