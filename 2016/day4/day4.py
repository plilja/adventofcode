import sys
from collections import Counter, namedtuple

Room = namedtuple('Room', 'encrypted_name sector_id checksum')

def parse_room(room_str):
    room_str = room_str.strip()
    parts = room_str.split('-')
    sector_id, checksum = parts[-1][:-1].split('[')
    sector_id = int(sector_id)
    encrypted_name = ''.join(parts[:-1]) 
    return Room(encrypted_name, sector_id, checksum)

def is_real_room(room):
    counter = Counter(room.encrypted_name)
    alphabet = [chr(ord('a') + i) for i in range(0, 26)]
    most_common = sorted(alphabet, key=lambda x: (-counter[x], x))
    for c1, c2 in zip(room.checksum, most_common):
        if c1 != c2:
            return False
    return True

def step1():
    ans = 0
    for line in sys.stdin.readlines():
        room = parse_room(line)
        if is_real_room(room):
            ans += room.sector_id
    return ans

print(step1())
