import sys

def has_abba_annotation(ip):
    c = 0
    abba_found = False
    abba_in_brackets_found = False
    
    for i in range(0, len(ip) - 4):
        if ip[i] == '[':
            c += 1
        elif ip[i] == ']':
            c -= 1
        else:
            sub = ip[i:i+4]
            if '[' not in sub and ']' not in sub and sub[:2] == sub[-1:-3:-1] and sub[0] != sub[1]:
                if c == 0:
                    abba_found = True
                else:
                    abba_in_brackets_found = True

    return abba_found and not abba_in_brackets_found


def step1(inp):
    return len(list(filter(has_abba_annotation, inp)))

inp = sys.stdin.readlines()
print(step1(inp))
