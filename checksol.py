#!/usr/bin/env python3

import filecmp
import glob
import os
import time
import random
from argparse import ArgumentParser

parser = ArgumentParser(description='Checks the solutions for a given day')
parser.add_argument('year')
parser.add_argument('day')
args = parser.parse_args()

day_padded = ('0' + args.day)[-2:]
input_search_path = 'y{}/day{}/input/*.in'.format(args.year, day_padded)
success = True
inputs_found = False

for input_file in glob.glob(input_search_path):
    inputs_found = True
    start = time.time()
    answer_tmp_file = '.answer-{}'.format(random.randint(0, 100000000000))
    os.system('python3 runner.py {} {} < {} > {}'.format(args.year, day_padded, input_file, answer_tmp_file))
    end = time.time()
    input_ans_file = input_file.replace(".in", ".ans")
    if not filecmp.cmp(input_ans_file, answer_tmp_file):
        success = False
        print(input_file + ', FAILED, execution time = {:.2f}'.format(end - start))
    else:
        print(input_file + ', success, execution time = {:.2f}'.format(end - start))
    if os.path.isfile(answer_tmp_file):
        os.remove(answer_tmp_file)
