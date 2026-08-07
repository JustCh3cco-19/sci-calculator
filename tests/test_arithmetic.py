import math
import unittest

from sci_calculator import arithmetic


class ArithmeticTests(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(arithmetic.add(2, 3), 5)
        self.assertEqual(arithmetic.subtract(7, 2), 5)
        self.assertEqual(arithmetic.multiply(4, 3), 12)
        self.assertEqual(arithmetic.divide(9, 3), 3)

    def test_division_by_zero_has_clear_error(self):
        with self.assertRaisesRegex(ValueError, "zero"):
            arithmetic.divide(1, 0)

    def test_logarithm_and_domains(self):
        self.assertAlmostEqual(arithmetic.logarithm(math.e), 1)
        with self.assertRaises(ValueError):
            arithmetic.logarithm(0)
        with self.assertRaises(ValueError):
            arithmetic.logarithm(10, 1)

    def test_square_root_domain(self):
        self.assertEqual(arithmetic.square_root(9), 3)
        with self.assertRaises(ValueError):
            arithmetic.square_root(-1)

    def test_angle_units(self):
        self.assertAlmostEqual(arithmetic.sine(90, "degrees"), 1)
        self.assertAlmostEqual(arithmetic.cosine(math.pi, "radians"), -1)
        self.assertAlmostEqual(arithmetic.arcsine(1, "degrees"), 90)
        self.assertAlmostEqual(arithmetic.arccosine(0, "degrees"), 90)
        self.assertAlmostEqual(arithmetic.arctangent(1, "degrees"), 45)
        with self.assertRaises(ValueError):
            arithmetic.tangent(90, "degrees")
        with self.assertRaises(ValueError):
            arithmetic.arcsine(2)

    def test_integer_operations(self):
        self.assertEqual(arithmetic.factorial(5), 120)
        self.assertEqual(arithmetic.gcd(18, 12), 6)
        self.assertEqual(arithmetic.lcm(6, 8), 24)
        with self.assertRaises(ValueError):
            arithmetic.factorial(-1)


if __name__ == "__main__":
    unittest.main()
