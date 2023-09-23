import sys
import re


FIELDS = ['byr',
          'iyr',
          'eyr',
          'hgt',
          'hcl',
          'ecl',
          'pid',
          'cid']


def parse(inp):
    result = [{}]
    for line in inp:
        if line == '':
            result.append({})
            continue
        for arg in line.split(' '):
            field, value = arg.split(':')
            result[-1][field] = value
    return result


def filter_correct_fields(passports):
    result = []
    for passport in passports:
        missing = list(filter(lambda f: f not in passport.keys(), FIELDS))
        if missing == [] or missing == ['cid']:
            result.append(passport)
    return result


def step1(inp):
    return len(filter_correct_fields(parse(inp)))


def step2(inp):
    result = 0
    for passport in filter_correct_fields(parse(inp)):
        if not (1920 <= int(passport['byr']) <= 2002):
            continue
        if not (2010 <= int(passport['iyr']) <= 2020):
            continue
        if not (2020 <= int(passport['eyr']) <= 2030):
            continue
        m = re.match(r'^(\d+)(cm|in)$', passport['hgt'])
        if not m:
            continue
        height, unit = m.groups()
        if unit == 'cm' and not (150 <= int(height) <= 193):
            continue
        if unit == 'in' and not (59 <= int(height) <= 76):
            continue
        if not re.match(r'^#[\da-z]{6}$', passport['hcl']):
            continue
        eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if passport['ecl'] not in eye_colors:
            continue
        if not re.match(r'^\d{9}$', passport['pid']):
            continue
        result += 1
    return result


inp = [line.strip() for line in sys.stdin.readlines()]
print(step1(inp))
print(step2(inp))
