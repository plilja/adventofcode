import sys
from collections import Counter


def step1(start_template, rules):
    return run_process(start_template, rules, 10)


def step2(start_template, rules):
    return run_process(start_template, rules, 40)


def run_process(template, rules, total_steps):
    pairs = Counter()
    for x, y in zip(template, template[1:]):
        pairs[x + y] += 1
    pairs[template[-1] + '|'] = 1  # end marker
    for i in range(0, total_steps):
        pairs2 = Counter()
        for pair, count in pairs.items():
            insert = rules.get(pair)
            if insert:
                pairs2[pair[0] + insert] += count
                pairs2[insert + pair[1]] += count
            else:
                pairs2[pair] += count
        pairs = pairs2
    chars = Counter()
    for pair, count in pairs.items():
        chars[pair[0]] += count
    mc = chars.most_common()
    return mc[0][1] - mc[-1][1]


def read_input():
    inp = sys.stdin.readlines()
    template = inp[0].strip()
    rules = {}
    for line in inp[2:]:
        args = line.split()
        rules[args[0]] = args[2]
    return template, rules


def main():
    template, rules = read_input()
    print(step1(template, rules))
    print(step2(template, rules))


if __name__ == '__main__':
    main()

