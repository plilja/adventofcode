#!/usr/bin/env python3
from argparse import ArgumentParser
from runpy import run_path

parser = ArgumentParser(description='''Runs a day''')
parser.add_argument('year')
parser.add_argument('day')
args = parser.parse_args()

program = args.year

day = ('0' + args.day)[-2:]
run_path('y{}/day{}/day{}.py'.format(args.year, day, day), run_name='__main__')
