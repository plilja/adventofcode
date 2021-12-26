import sys
from collections import Counter


def step1(start_template, rules):
    return run_process(start_template, rules, 10)


def step2(start_template, rules):
    return run_process(start_template, rules, 40)


def run_process(start_template, rules, total_steps):
    def helper(template, steps, cache):
        key = (template, steps)
        if key in cache:
            return cache[key]
        elif steps == 0:
            result = Counter(template)
        elif len(template) <= 3:
            new_template = template[0]
            for x, y in zip(template, template[1:]):
                insert = rules.get(x + y, '')
                new_template += insert
                new_template += y
            result = helper(new_template, steps - 1, cache)
        else:
            a = template[:len(template) // 2]
            b = template[len(template) // 2:]
            joint = a[-1] + b[0]
            result = Counter()
            insert = rules.get(joint)
            if insert:
                result += helper(joint, steps, cache)
                result[joint[0]] -= 1
                result[joint[1]] -= 1
            result += helper(a, steps, cache)
            result += helper(b, steps, cache)
        cache[key] = result
        return result

    mc = helper(start_template, total_steps, {}).most_common()
    return mc[0][1] - mc[-1][1]


def read_input():
    inp = sys.stdin.readlines()
    template = inp[0].strip()
    rules = {}
    for line in inp[2:]:
        args = line.split()
        rules[args[0]] = args[2]
    return template, rules


template, rules = read_input()
print(step1(template, rules))
print(step2(template, rules))
