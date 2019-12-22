import sys
from collections import namedtuple, defaultdict
from math import ceil

Amount = namedtuple('Amount', 'amount chemical')
Reaction = namedtuple('Reaction', 'inputs output')


def step1(reactions):
    output_to_reaction = {}
    for reaction in reactions:
        output_to_reaction[reaction.output.chemical] = reaction

    state = defaultdict(int)
    state['FUEL'] = -1
    debt = ['FUEL']
    while debt:
        debt_chemical = debt[0]
        debt = debt[1:]
        debt_amount = -state[debt_chemical]
        if state[debt_chemical] < 0:
            reaction = output_to_reaction[debt_chemical]
            t = ceil(debt_amount / reaction.output.amount)
            for amount in reaction.inputs:
                state[amount.chemical] -= t * amount.amount
                if amount.chemical != 'ORE' and state[amount.chemical] < 0:
                    debt.append(amount.chemical)
            state[debt_chemical] += t * reaction.output.amount
    return -state['ORE']


def read_input():
    def parse_amount(s):
        amount, chemical = s.strip().split(' ')
        return Amount(int(amount), chemical)

    reactions = []
    for raw_arg in sys.stdin.readlines():
        inputs_raw, output_raw = raw_arg.split(' => ')
        inputs = []
        for s in inputs_raw.split(','):
            inputs.append(parse_amount(s))
        output = parse_amount(output_raw)
        reactions.append(Reaction(inputs, output))
    return reactions


reactions = read_input()
print(step1(reactions))
