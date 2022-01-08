import atexit
import sys
from functools import wraps
from time import time

_TIMERS = {}
_INVOCATIONS = {}


def timed(f):
    name = f.__name__
    if name not in _TIMERS:
        _TIMERS[name] = 0
        _INVOCATIONS[name] = 0

    @wraps(f)
    def wrap(*args, **kw):
        start = time()
        result = f(*args, **kw)
        end = time()
        _TIMERS[name] += end - start
        _INVOCATIONS[name] += 1
        return result

    return wrap


def print_timings():
    for name in _TIMERS.keys():
        print('Timers function={} invocationCount={} totalDuration={:.4f}s'.format(name, _INVOCATIONS[name],
                                                                                   _TIMERS[name]),
              file=sys.stderr)


atexit.register(print_timings)
