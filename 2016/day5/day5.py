import hashlib
import sys

def step1(door_id):
    j = 0
    ans = ''
    for i in range(0, 8):
        while True:
            digest = md5(door_id + str(j))
            j += 1
            if digest[:5] == '00000':
                ans += digest[5]
                break
    return ans


def md5(v):
    m = hashlib.md5()
    m.update(v.encode('utf-8'))
    return m.hexdigest()

door_id = input().strip()
print(step1(door_id))
