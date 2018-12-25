import sys
import re
from collections import namedtuple
from enum import Enum
from math import *

Group = namedtuple('Group', 'type id units hit_points weaknesses immunities attack_damage attack_type initiative')

class Type(Enum):
    IMMUNE_SYSTEM = 1
    INFECTION = 2


def get(groups, t):
    return list(filter(lambda x: x.type == t, groups))


def step1(groups):
    rem_groups = groups[::]
    while get(rem_groups, Type.IMMUNE_SYSTEM) != [] and get(rem_groups, Type.INFECTION) != []:
        rem_groups.sort(key=lambda x: (-x.units*x.attack_damage, -x.initiative))
        selections = {}
        for group in rem_groups:
            highest_target = None
            highest_damage = 0
            highest_effective_power = 0
            for target in rem_groups:
                if group.type != target.type and target not in selections.values():
                    damage = group.units * determine_damage(group, target)
                    effective_power = target.units * target.attack_damage
                    if (damage, effective_power) > (highest_damage, highest_effective_power):
                        highest_damage = damage
                        highest_effective_power = effective_power
                        highest_target = target
            if highest_target != None and highest_damage > 0:
                selections[group.id] = highest_target

        rem_groups.sort(key=lambda x: -x.initiative)

        next_groups = {group.id:group for group in rem_groups}
        for group in rem_groups:
            if group.id in selections and group.id in next_groups:
                group = next_groups[group.id]
                target = selections[group.id]
                damage = determine_damage(group, target)
                killed = min(target.units, (group.units * damage) // target.hit_points)
                remaining = target.units - killed
                if remaining > 0:
                    d = target._asdict()
                    del d['units']
                    next_groups[target.id] = Group(units=remaining, **d)
                else:
                    del next_groups[target.id]
        rem_groups = list(next_groups.values())
    return sum([g.units for g in rem_groups])


def determine_damage(group, target):
    assert group.type != target.type
    if group.attack_type in target.immunities:
        damage = 0
    elif group.attack_type in target.weaknesses:
        damage = 2 * group.attack_damage
    else:
        damage = group.attack_damage
    return damage


def parse_input():
    groups = []
    i = 1
    for s in sys.stdin:
        s = s.strip()
        if s == 'Immune System:':
            type_ = Type.IMMUNE_SYSTEM
        elif s == 'Infection:':
            type_ = Type.INFECTION
        elif s:
            args = re.match(r'(\d+)[^\d]*(\d+)[^\d]*(\d+) ([^ ]+) damage[^\d]*(\d+)', s).groups()
            units = int(args[0])
            hit_points = int(args[1])
            weaknesses = []
            immunities = []
            if 'weak to' in s:
                weaknesses = re.match(r'.*weak to ([^;\)]+)', s).groups()[0].split(', ')
            if 'immune to' in s:
                immunities = re.match(r'.*immune to ([^;\)]+)', s).groups()[0].split(', ')
            attack_damage = int(args[2])
            attack_type = args[3]
            initiative = int(args[4])
            g = Group(type_, i, units, hit_points, weaknesses, immunities, 
                    attack_damage, attack_type, initiative)
            i += 1
            groups.append(g)
    return groups

groups = parse_input()
print(step1(groups))

