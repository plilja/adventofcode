import sys

wires = {}
computed = {}

for i in range(0, 65536):
    def f(j):
        return lambda: j


    wires[str(i)] = f(i)

for line in sys.stdin.readlines():
    def cache(key, f):
        def g():
            if key in computed:
                return computed[key]
            else:
                r = f()
                computed[key] = r
                return r

        wires[key] = g


    def parse(args):
        if args[0] == 'NOT':
            cache(args[3], lambda: ~(wires[args[1]]()) % 65536)
        elif args[1] == '->':
            if args[0].isdigit():
                cache(args[2], lambda: int(args[0]) % 65536)
            else:
                cache(args[2], lambda: wires[args[0]]() % 65536)
        elif args[1] == 'AND':
            cache(args[4], lambda: (wires[args[0]]() & wires[args[2]]()) % 65536)
        elif args[1] == 'OR':
            cache(args[4], lambda: (wires[args[0]]() | wires[args[2]]()) % 65536)
        elif args[1] == 'LSHIFT':
            cache(args[4], lambda: (wires[args[0]]() << int(args[2])) % 65536)
        elif args[1] == 'RSHIFT':
            cache(args[4], lambda: (wires[args[0]]() >> int(args[2])) % 65536)


    parse(line.split())

step1 = wires['a']()
computed.clear()
wires['b'] = lambda: step1
step2 = wires['a']()

print(step1)
print(step2)
