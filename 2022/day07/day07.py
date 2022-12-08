import sys
import re
from collections import namedtuple, deque

Dir = namedtuple('Dir', 'name parent files dirs')


def step1(inp):
    root = parse(inp)
    sizes = {}
    result = 0
    q = deque([root])
    while q:
        directory = q.popleft()
        size = get_size(directory, sizes)
        if size <= 100000:
            result += size
        for key, value in directory.dirs.items():
            q.append(value)
    return result


def get_size(directory, cache):
    p = path(directory)
    if p in cache:
        return cache[p]
    result = 0
    for key, value in directory.dirs.items():
        result += get_size(value, cache)
    for key, value in directory.files.items():
        result += value
    cache[p] = result
    return result


def parse(inp):
    root = Dir('', None, {}, {})
    current_dir = root
    i = 0
    while i < len(inp):
        command = inp[i]
        if command[0] != '$':
            raise ValueError('Command must start with $ got ' + command)
        program, argument = re.match(r'\$ ([a-z]+) ?(.*)', command).groups()
        if program == 'cd':
            current_dir = cd(current_dir, argument)
            i += 1
        elif program == 'ls':
            i = ls(current_dir, inp, i)
    return root


def cd(current_dir, name):
    if name == '/':
        while current_dir.parent is not None:
            current_dir = current_dir.parent
        return current_dir
    elif name == '..':
        return current_dir.parent
    if name not in current_dir.dirs:
        current_dir.dirs[name] = Dir(name, current_dir, {}, {})
    return current_dir.dirs[name]


def ls(current_dir, inp, i):
    i += 1
    while i < len(inp) and inp[i][0] != '$':
        a, b = inp[i].split(' ')
        if a != 'dir':
            size = int(a)
            name = b
            current_dir.files[name] = size
        i += 1
    return i


def path(directory):
    parts = []
    while directory is not None:
        parts.append(directory.name)
        directory = directory.parent
    parts.reverse()
    return '/'.join(parts)


inp = list(map(str.strip, sys.stdin.readlines()))
print(step1(inp))
