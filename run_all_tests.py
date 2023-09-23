#!/usr/bin/python

import os
from concurrent.futures import ProcessPoolExecutor
import multiprocessing


def test(year, day):
    day_padded = ('0' + day)[-2:]
    if os.path.exists('./y{}/day{}/day{}.py'.format(year, day_padded, day_padded)):
        os.system('./checksol.py {} {}'.format(year, day))


def run():
    print(os.getcwd())
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        futures = []
        for d in sorted(os.listdir(os.getcwd())):
            try:
                if os.path.isdir(d):
                    year = d[1:]
                    int(year)  # check that it is an integer (yYYYY)
                    for f in sorted(os.listdir(d)):
                        if f.startswith('day') and os.path.isdir(d + '/' + f):
                            day = f.replace('day', '')
                            future = executor.submit(test, year, day)
                            futures.append(future)
            except ValueError:
                pass  # just ignore
        for future in futures:
            future.result()


if __name__ == '__main__':
    run()
