#!/usr/bin/python

import os

def test(f):
    p = os.getcwd()
    os.chdir(f)
    pys = list(filter(lambda f: f.endswith('.py'), os.listdir('.')))
    if pys:
        print(f + '/' + pys[0])
        os.system('~/workspace/algolib/util/checksol.py %s -e python3' % pys[0])
    os.chdir(p)

def run():
    print(os.getcwd())
    for year in ['2015', '2016', '2017', '2018']:
        for f in os.listdir(year):
            if os.path.isdir(year + '/' + f):
                #print('./' + year + '/' + f)
                test('./' + year + '/' + f)

if __name__ == '__main__':
    run()
