import unittest
from polynomial import Polynomial


class PolynomialBasicTest(unittest.TestCase):
    def test_add(self):
        a, b, c = Polynomial([1, 2, 3]), Polynomial([3, 2, 1]), Polynomial([4, 4, 4])
        self.assertEqual(c, a + b)

    def test_sub(self):
        a, b, c = Polynomial([1, 2, 3]), Polynomial([3, 2, 1]), Polynomial([-2, 0, 2])
        self.assertEqual(c, a - b)

    def test_mul(self):
        a, b, c = Polynomial([1, 1]), Polynomial([1, -1]), Polynomial([1, 0, -1])
        self.assertEqual(c, a * b)

    def test_add_constant(self):
        a, b, c = Polynomial([1, 2, 3]), 5, Polynomial([1, 2, 8])
        self.assertEqual(c, a + b)

    def test_sub_constant(self):
        a, b, c = Polynomial([1, 2, 3]), 4, Polynomial([1, 2, -1])
        self.assertEqual(c, a - b)

    def test_mul_constant(self):
        a, b, c = Polynomial([1, 0, 1]), 3, Polynomial([3, 0, 3])
        self.assertEqual(c, a * b)

    def test_add2(self):
        a, b = Polynomial([1, 2, 3]), Polynomial([-1, -2, -3])
        self.assertEqual(a + b, Polynomial([0]))

    def test_sub2(self):
        a, b = Polynomial([1, 2, 3]), Polynomial([1, 2, 3])
        self.assertEqual(a - b, Polynomial([0]))

    def test_mul2(self):
        a = Polynomial([2, 3, 0])
        a = a * 0
        self.assertEqual(a, Polynomial([0, 0, 0]))


class PolynomialExTest(unittest.TestCase):
    def test_equal1(self):
        self.assertEqual(Polynomial([1, 1, 1]), Polynomial([1, 1, 1]))

    def test_equal2(self):
        self.assertEqual(Polynomial([1, 0, 1]), Polynomial([0, 1, 0, 1]))

    def test_not_equal1(self):
        self.assertNotEqual(Polynomial([1, 0, 1]), Polynomial([1, 1, 1]))

    def test_not_equal2(self):
        self.assertNotEqual(Polynomial([2, 2, 0]), Polynomial([2, 2]))

    def test_equal_null1(self):
        self.assertEqual(Polynomial([0, 0]), Polynomial([0]))

    def test_equal_null2(self):
        self.assertEqual(Polynomial([0, 0]), Polynomial([]))

    def test_equal_constant1(self):
        self.assertEqual(Polynomial([0, 8]), 8)

    def test_equal_constant2(self):
        self.assertEqual(Polynomial([0, 0]), 0)




if __name__ == '__main__':
    unittest.main()