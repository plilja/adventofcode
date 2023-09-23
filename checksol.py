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
test_search_path = 'y{}/day{}/test/*.in'.format(args.year, day_padded)
success = True
tests_found = False

for test_file in glob.glob(test_search_path):
    tests_found = True
    start = time.time()
    answer_tmp_file = '.answer-{}'.format(random.randint(0, 100000000000))
    os.system('python3 runner.py {} {} < {} > {}'.format(args.year, day_padded, test_file, answer_tmp_file))
    end = time.time()
    test_exp_file = test_file.replace(".in", ".ans")
    if not filecmp.cmp(test_exp_file, answer_tmp_file):
        success = False
        print(test_file + ', FAILED, execution time = {:.2f}'.format(end - start))
    else:
        print(test_file + ', success, execution time = {:.2f}'.format(end - start))
    if os.path.isfile(answer_tmp_file):
        os.remove(answer_tmp_file)
