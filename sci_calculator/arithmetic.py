"""Numeric arithmetic and trigonometric operations."""

from __future__ import annotations

import math
from typing import Literal

AngleUnit = Literal["degrees", "radians"]


def add(left: float, right: float) -> float:
    return left + right


def subtract(left: float, right: float) -> float:
    return left - right


def multiply(left: float, right: float) -> float:
    return left * right


def divide(left: float, right: float) -> float:
    if right == 0:
        raise ValueError("Non è possibile dividere per zero.")
    return left / right


def power(base: float, exponent: float) -> float | complex:
    return base**exponent


def square_root(value: float) -> float:
    if value < 0:
        raise ValueError("La radice quadrata reale richiede un numero non negativo.")
    return math.sqrt(value)


def logarithm(value: float, base: float = math.e) -> float:
    if value <= 0:
        raise ValueError("Il logaritmo richiede un argomento positivo.")
    if base <= 0 or base == 1:
        raise ValueError("La base deve essere positiva e diversa da 1.")
    return math.log(value, base)


def _angle(value: float, unit: AngleUnit) -> float:
    if unit == "degrees":
        return math.radians(value)
    if unit == "radians":
        return value
    raise ValueError("L'unità deve essere 'degrees' oppure 'radians'.")


def sine(value: float, unit: AngleUnit = "radians") -> float:
    return math.sin(_angle(value, unit))


def cosine(value: float, unit: AngleUnit = "radians") -> float:
    return math.cos(_angle(value, unit))


def tangent(value: float, unit: AngleUnit = "radians") -> float:
    angle = _angle(value, unit)
    if math.isclose(math.cos(angle), 0.0, abs_tol=1e-12):
        raise ValueError("La tangente non è definita per questo angolo.")
    return math.tan(angle)


def _inverse_angle(value: float, unit: AngleUnit) -> float:
    if unit == "radians":
        return value
    if unit == "degrees":
        return math.degrees(value)
    raise ValueError("L'unità deve essere 'degrees' oppure 'radians'.")


def arcsine(value: float, unit: AngleUnit = "radians") -> float:
    if not -1 <= value <= 1:
        raise ValueError("L'arcoseno richiede un valore compreso tra -1 e 1.")
    return _inverse_angle(math.asin(value), unit)


def arccosine(value: float, unit: AngleUnit = "radians") -> float:
    if not -1 <= value <= 1:
        raise ValueError("L'arcocoseno richiede un valore compreso tra -1 e 1.")
    return _inverse_angle(math.acos(value), unit)


def arctangent(value: float, unit: AngleUnit = "radians") -> float:
    return _inverse_angle(math.atan(value), unit)


def factorial(value: int) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError("Il fattoriale richiede un intero non negativo.")
    return math.factorial(value)


def gcd(left: int, right: int) -> int:
    return math.gcd(left, right)


def lcm(left: int, right: int) -> int:
    return math.lcm(left, right)


def compare(left: float, right: float) -> str:
    if left == right:
        return "uguale a"
    return "minore di" if left < right else "maggiore di"
