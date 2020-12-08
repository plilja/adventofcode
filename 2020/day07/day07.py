import sys
import re
from collections import namedtuple, deque, defaultdict

Rule = namedtuple('Rule', 'bag contents')


def parse(inp):
    result = []
    for line in inp:
        bag_name, contents_str = line.split(' bags contain ')
        contents = {}
        if 'no other bag' not in contents_str:
            for content_bag in contents_str.split(','):
                num, content_bag_name = re.match(' *(\\d+) (\\w+ \\w+) bags?\\.? *', content_bag).groups()
                contents[content_bag_name] = int(num)
        result.append(Rule(bag_name, contents))
    return result


def step1(rules):
    graph = defaultdict(list)
    for rule in rules:
        for bag, num in rule.contents.items():
            graph[bag].append(rule.bag)
    q = deque(['shiny gold'])
    colors = set()
    while q:
        p = q.popleft()
        colors.add(p)
        for parent in graph[p]:
            q.append(parent)
    return len(colors) - 1  # subtract 1 to remove shiny gold itself


rules = parse([line.strip() for line in sys.stdin.readlines()])
print(step1(rules))
