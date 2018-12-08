from collections import namedtuple

Node = namedtuple('Node', 'children metadata')

def parse(inp):
    def f(s):
        num_children = s.pop()
        num_meta = s.pop()
        children = []
        meta = []
        for i in range(0, num_children):
            children.append(f(s))
        for i in range(0, num_meta):
            meta.append(s.pop())
        return Node(children, meta)

    s = list(reversed(inp))
    return f(s)

def step1(inp):
    def sum_meta(node):
        a = sum(node.metadata)
        b = sum(map(sum_meta, node.children))
        return a + b
    return sum_meta(parse(inp))


inp = list(map(int, input().split()))
print(step1(inp))
