#!/usr/bin/python

import os
from concurrent.futures import ProcessPoolExecutor
import multiprocessing


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
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        futures = []
        for d in sorted(os.listdir(os.getcwd())):
            try:
                if os.path.isdir(d):
                    int(d)  # check that it is an integer
                    for f in sorted(os.listdir(d)):
                        if f.startswith('day') and os.path.isdir(d + '/' + f):
                            future = executor.submit(test, './' + d + '/' + f)
                            futures.append(future)
            except ValueError:
                pass  # just ignore
        for future in futures:
            future.result()


if __name__ == '__main__':
    run()
