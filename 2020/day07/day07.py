import sys
import re
from collections import deque, defaultdict


def parse(inp):
    result = {}
    for line in inp:
        bag_name, contents_str = line.split(' bags contain ')
        contents = {}
        if 'no other bag' not in contents_str:
            for sub_bag_str in contents_str.split(','):
                num, sub_bag_name = re.match(' *(\\d+) (\\w+ \\w+) bags?\\.? *', sub_bag_str).groups()
                contents[sub_bag_name] = int(num)
        result[bag_name] = contents
    return result


def step1(rules):
    graph = defaultdict(list)
    for bag, contents in rules.items():
        for sub_bag, num in contents.items():
            graph[sub_bag].append(bag)
    q = deque(['shiny gold'])
    colors = set()
    while q:
        p = q.popleft()
        colors.add(p)
        for parent in graph[p]:
            q.append(parent)
    return len(colors) - 1  # subtract 1 to remove shiny gold itself


def step2(rules):
    cache = {}

    def dfs(bag):
        if bag in cache:
            return cache[bag]
        else:
            cost = 1  # the cost of the bag itself
            for sub_bag, num in rules[bag].items():
                cost += num * dfs(sub_bag)
            cache[bag] = cost
            return cost
    return dfs('shiny gold') - 1


rules = parse([line.strip() for line in sys.stdin.readlines()])
print(step1(rules))
print(step2(rules))
