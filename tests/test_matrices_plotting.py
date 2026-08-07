import unittest

import matplotlib
import sympy as sp

matplotlib.use("Agg")

from sci_calculator.matrices import determinant, inverse, multiply, parse_matrix
from sci_calculator.plotting import plot_expression


class MatrixTests(unittest.TestCase):
    def test_parse_and_operations(self):
        matrix = parse_matrix("[[1, 2], [3, 4]]")
        self.assertEqual(matrix, sp.Matrix([[1, 2], [3, 4]]))
        self.assertEqual(determinant(matrix), -2)
        expected_inverse = sp.Matrix([[-2, 1], [sp.Rational(3, 2), sp.Rational(-1, 2)]])
        self.assertEqual(inverse(matrix), expected_inverse)
        self.assertEqual(multiply(matrix, "[[1], [0]]"), sp.Matrix([[1], [3]]))

    def test_matrix_errors(self):
        with self.assertRaises(ValueError):
            parse_matrix("[[1], [2, 3]]")
        with self.assertRaises(ValueError):
            determinant("[[1, 2, 3]]")
        with self.assertRaises(ValueError):
            inverse("[[1, 2], [2, 4]]")
        with self.assertRaises(ValueError):
            multiply("[[1, 2]]", "[[1, 2]]")


class PlottingTests(unittest.TestCase):
    def test_plot_uses_requested_expression_and_range(self):
        figure = plot_expression("x**2", lower=-2, upper=2, show=False)
        axes = figure.axes[0]
        self.assertEqual(axes.get_title(), "Grafico di x**2")
        self.assertEqual(tuple(axes.lines[0].get_xdata()[[0, -1]]), (-2, 2))

    def test_plot_rejects_extra_symbols_and_bad_range(self):
        with self.assertRaises(ValueError):
            plot_expression("x+y", show=False)
        with self.assertRaises(ValueError):
            plot_expression("x", lower=1, upper=1, show=False)


if __name__ == "__main__":
    unittest.main()
