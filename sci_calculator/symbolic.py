"""Symbolic calculus, algebra and equation solving with SymPy."""

from __future__ import annotations

import ast

import sympy as sp

KNOWN_SYMBOLS = {name: sp.Symbol(name) for name in ("x", "y", "z", "t")}
LOCALS = {
    **KNOWN_SYMBOLS,
    "pi": sp.pi,
    "e": sp.E,
    "E": sp.E,
    "oo": sp.oo,
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "asin": sp.asin,
    "acos": sp.acos,
    "atan": sp.atan,
    "sqrt": sp.sqrt,
    "log": sp.log,
    "exp": sp.exp,
    "Abs": sp.Abs,
}

_ALLOWED_AST_NODES = (
    ast.Expression,
    ast.BinOp,
    ast.UnaryOp,
    ast.Call,
    ast.Name,
    ast.Load,
    ast.Constant,
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.Pow,
    ast.Mod,
    ast.UAdd,
    ast.USub,
)


def _validate_expression_syntax(expression: str) -> None:
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as error:
        raise ValueError(f"Espressione non valida: {expression}") from error
    for node in ast.walk(tree):
        if not isinstance(node, _ALLOWED_AST_NODES):
            raise ValueError("L'espressione contiene una sintassi non consentita.")
        if isinstance(node, ast.Name) and node.id.startswith("_"):
            raise ValueError("I nomi che iniziano con '_' non sono consentiti.")
        if isinstance(node, ast.Call) and (
            not isinstance(node.func, ast.Name) or node.func.id not in LOCALS
        ):
            raise ValueError("La funzione richiesta non è supportata.")


def parse_expression(expression: str | sp.Expr) -> sp.Expr:
    if isinstance(expression, sp.Expr):
        return expression
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("Inserisci un'espressione non vuota.")
    normalized = expression.strip().replace("^", "**")
    _validate_expression_syntax(normalized)
    try:
        parsed = sp.sympify(normalized, locals=LOCALS)
    except (sp.SympifyError, SyntaxError, TypeError) as error:
        raise ValueError(f"Espressione non valida: {expression}") from error
    if not isinstance(parsed, sp.Expr):
        raise ValueError("L'input non rappresenta un'espressione matematica.")
    return parsed


def symbol(name: str) -> sp.Symbol:
    name = name.strip()
    if not name.isidentifier():
        raise ValueError("Il nome della variabile non è valido.")
    return KNOWN_SYMBOLS.get(name, sp.Symbol(name))


def parse_bound(value: str | float | int | sp.Expr) -> sp.Expr:
    if isinstance(value, (float, int)):
        return sp.sympify(value)
    return parse_expression(value)


def integrate(
    expression: str | sp.Expr,
    variable: str = "x",
    lower: str | float | int | sp.Expr | None = None,
    upper: str | float | int | sp.Expr | None = None,
) -> sp.Expr:
    expr = parse_expression(expression)
    var = symbol(variable)
    if (lower is None) != (upper is None):
        raise ValueError("Specifica entrambi gli estremi oppure nessuno.")
    if lower is None:
        return sp.integrate(expr, var)
    return sp.integrate(expr, (var, parse_bound(lower), parse_bound(upper)))


def multiple_integral(
    expression: str | sp.Expr,
    bounds: list[tuple[str, str | float | int, str | float | int]],
) -> sp.Expr:
    expr = parse_expression(expression)
    limits = [(symbol(name), parse_bound(low), parse_bound(high)) for name, low, high in bounds]
    return sp.integrate(expr, *limits)


def differentiate(expression: str | sp.Expr, variable: str = "x", order: int = 1) -> sp.Expr:
    if order < 1:
        raise ValueError("L'ordine della derivata deve essere almeno 1.")
    return sp.diff(parse_expression(expression), symbol(variable), order)


def limit(
    expression: str | sp.Expr,
    variable: str = "x",
    point: str | float | int | sp.Expr = "oo",
    direction: str = "+-",
) -> sp.Expr:
    if direction not in {"+", "-", "+-"}:
        raise ValueError("La direzione deve essere '+', '-' oppure '+-'.")
    return sp.limit(
        parse_expression(expression),
        symbol(variable),
        parse_bound(point),
        dir=direction,
    )


def solve_equation(expression: str, variable: str = "x") -> list[sp.Expr]:
    var = symbol(variable)
    if "=" in expression:
        left, right = expression.split("=", maxsplit=1)
        equation = sp.Eq(parse_expression(left), parse_expression(right))
    else:
        equation = parse_expression(expression)
    return sp.solve(equation, var)


def expand(expression: str | sp.Expr) -> sp.Expr:
    return sp.expand(parse_expression(expression))


def prime_factors(value: int) -> dict[int, int]:
    if value == 0:
        raise ValueError("Zero non ammette una scomposizione finita in fattori primi.")
    return sp.factorint(value)
