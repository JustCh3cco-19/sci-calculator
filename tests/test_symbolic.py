import unittest

import sympy as sp

from sci_calculator.symbolic import (
    differentiate,
    expand,
    integrate,
    limit,
    multiple_integral,
    parse_expression,
    solve_equation,
)


class SymbolicTests(unittest.TestCase):
    def test_parser_accepts_caret_and_constants(self):
        x = sp.Symbol("x")
        self.assertEqual(parse_expression("x^2 + pi"), x**2 + sp.pi)

    def test_indefinite_and_symbolic_definite_integrals(self):
        x = sp.Symbol("x")
        self.assertEqual(integrate("x**2"), x**3 / 3)
        self.assertEqual(integrate("sin(x)", lower="0", upper="pi"), 2)

    def test_multiple_integrals(self):
        self.assertEqual(
            multiple_integral("x+y", [("x", 0, 1), ("y", 0, 1)]),
            1,
        )
        self.assertEqual(
            multiple_integral("1", [("x", 0, 2), ("y", 0, 3), ("z", 0, 4)]),
            24,
        )

    def test_derivative_limit_and_expansion(self):
        x = sp.Symbol("x")
        self.assertEqual(differentiate("sin(x)"), sp.cos(x))
        self.assertEqual(differentiate("x**3", order=2), 6 * x)
        self.assertEqual(limit("1/x", point="oo"), 0)
        self.assertEqual(expand("(x+1)^2"), x**2 + 2 * x + 1)

    def test_equation_with_equal_sign_and_multiple_solutions(self):
        self.assertEqual(solve_equation("x^2 = 4"), [-2, 2])
        self.assertEqual(solve_equation("exp(x) = 0"), [])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            parse_expression("")
        with self.assertRaises(ValueError):
            integrate("x", lower=0)
        with self.assertRaises(ValueError):
            differentiate("x", order=0)
        with self.assertRaises(ValueError):
            parse_expression("__import__('os').getcwd()")
        with self.assertRaises(ValueError):
            parse_expression("open('/tmp/example')")


if __name__ == "__main__":
    unittest.main()
