"""Reusable scientific-calculator library."""

from .arithmetic import (
    add,
    arccosine,
    arcsine,
    arctangent,
    compare,
    cosine,
    divide,
    factorial,
    gcd,
    lcm,
    logarithm,
    multiply,
    power,
    sine,
    square_root,
    subtract,
    tangent,
)
from .symbolic import differentiate, expand, integrate, limit, solve_equation

__all__ = [
    "add",
    "arccosine",
    "arcsine",
    "arctangent",
    "compare",
    "cosine",
    "differentiate",
    "divide",
    "expand",
    "factorial",
    "gcd",
    "integrate",
    "lcm",
    "limit",
    "logarithm",
    "multiply",
    "power",
    "sine",
    "solve_equation",
    "square_root",
    "subtract",
    "tangent",
]

__version__ = "2.0.0"
