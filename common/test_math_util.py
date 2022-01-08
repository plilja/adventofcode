from unittest import TestCase

from common.math_util import sign


class Test(TestCase):
    def test_sign(self):
        self.assertEqual(1, sign(1))
        self.assertEqual(1, sign(2))
        self.assertEqual(0, sign(0))
        self.assertEqual(-1, sign(-1))
        self.assertEqual(-1, sign(-2))
