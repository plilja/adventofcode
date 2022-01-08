from unittest import TestCase

from common.util import ever


class Test(TestCase):
    def test_ever(self):
        j = 0
        for i in ever():
            self.assertEqual(j, i)
            j += 1
            if j > 200:
                break
