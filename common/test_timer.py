from unittest import TestCase

from common.timer import timed


@timed
def fib(n):
    ls = [1, 1]
    if n == 0:
        return 0
    if n <= 2:
        return ls[n - 1]
    for i in range(3, n + 1):
        tmp = ls[1]
        ls[1] = ls[0] + ls[1]
        ls[0] = tmp
    return ls[-1]


class Test(TestCase):
    def test_timed(self):
        # timed should not do anything to the decorated method,
        # just make some calls to verify that the function works unaffected
        self.assertEqual(0, fib(0))
        self.assertEqual(1, fib(1))
        self.assertEqual(1, fib(2))
        self.assertEqual(2, fib(3))
        self.assertEqual(3, fib(4))
        self.assertEqual(5, fib(5))
