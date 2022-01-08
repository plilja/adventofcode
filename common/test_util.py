from unittest import TestCase

from common.util import ever, traced, manhattan


@traced
def add3(n):
    return n + 3


class Test(TestCase):
    def test_ever(self):
        j = 0
        for i in ever():
            self.assertEqual(j, i)
            j += 1
            if j > 200:
                break

    def test_traced(self):
        add3(0)
        add3(3)

    def test_manhattan(self):
        self.assertEqual(4, manhattan((0, 2), (2, 0)))
        self.assertEqual(0, manhattan((0, 0), (0, 0)))
        self.assertEqual(2, manhattan((0, -2), (0, 0)))
        self.assertEqual(2, manhattan((0, 0), (-2, 0)))
