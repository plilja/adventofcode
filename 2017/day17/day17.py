
def step1(n):
    buf = [0]
    pos = 0
    for val in range(1, 2018):
        pos = (pos + n) % len(buf)
        pos += 1
        buf = buf[:pos] + [val] + buf[pos:]

    return buf[(pos + 1) % len(buf)]
        

n = int(input())
print(step1(n))
