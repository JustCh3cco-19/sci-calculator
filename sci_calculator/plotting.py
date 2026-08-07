"""Expression plotting utilities."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from .symbolic import parse_expression, symbol


def plot_expression(
    expression: str,
    variable: str = "x",
    lower: float = -10,
    upper: float = 10,
    *,
    show: bool = True,
):
    if lower >= upper:
        raise ValueError("Il limite inferiore deve essere minore di quello superiore.")
    expr = parse_expression(expression)
    var = symbol(variable)
    unsupported = expr.free_symbols - {var}
    if unsupported:
        raise ValueError("Il grafico può contenere una sola variabile libera.")

    function = __import__("sympy").lambdify(var, expr, modules=["numpy"])
    x_values = np.linspace(lower, upper, 2000)
    with np.errstate(all="ignore"):
        y_values = np.asarray(function(x_values))
    if y_values.ndim == 0:
        y_values = np.full_like(x_values, y_values, dtype=float)

    figure, axes = plt.subplots()
    axes.plot(x_values, y_values, label=str(expr))
    axes.axhline(0, color="black", linewidth=0.8)
    axes.axvline(0, color="black", linewidth=0.8)
    axes.set(xlabel=variable, ylabel="f(x)", title=f"Grafico di {expr}")
    axes.grid(True, alpha=0.3)
    axes.legend()
    if show:
        plt.show()
    return figure
