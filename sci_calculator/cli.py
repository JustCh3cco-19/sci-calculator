"""Interactive command-line interface."""

from __future__ import annotations

import math
from collections.abc import Callable

import sympy as sp

from . import arithmetic
from .matrices import determinant, inverse, parse_matrix
from .matrices import multiply as matrix_multiply
from .plotting import plot_expression
from .symbolic import (
    differentiate,
    expand,
    integrate,
    limit,
    multiple_integral,
    prime_factors,
    solve_equation,
)


def _text(prompt: str) -> str:
    value = input(prompt).strip()
    if not value:
        raise ValueError("Il valore non può essere vuoto.")
    return value


def _float(prompt: str) -> float:
    try:
        return float(_text(prompt))
    except ValueError as error:
        raise ValueError("Inserisci un numero valido.") from error


def _int(prompt: str) -> int:
    try:
        return int(_text(prompt))
    except ValueError as error:
        raise ValueError("Inserisci un numero intero valido.") from error


def _binary(operation: Callable[[float, float], object], symbol: str) -> None:
    left = _float("Primo numero: ")
    right = _float("Secondo numero: ")
    print(f"{left} {symbol} {right} = {operation(left, right)}")


def arithmetic_menu() -> None:
    operations = {
        "+": arithmetic.add,
        "-": arithmetic.subtract,
        "*": arithmetic.multiply,
        "/": arithmetic.divide,
        "^": arithmetic.power,
    }
    operator = _text("Operatore (+, -, *, /, ^): ")
    if operator not in operations:
        raise ValueError("Operatore non valido.")
    _binary(operations[operator], operator)


def roots_and_logs() -> None:
    choice = _text("Operazione (sqrt/ln/log): ").lower()
    value = _float("Valore: ")
    if choice == "sqrt":
        print(arithmetic.square_root(value))
    elif choice == "ln":
        print(arithmetic.logarithm(value))
    elif choice == "log":
        print(arithmetic.logarithm(value, _float("Base: ")))
    else:
        raise ValueError("Operazione non valida.")


def trigonometry() -> None:
    functions = {
        "sin": arithmetic.sine,
        "cos": arithmetic.cosine,
        "tan": arithmetic.tangent,
    }
    name = _text("Funzione (sin/cos/tan/sec/cot/csc/asin/acos/atan): ").lower()
    value = _float("Angolo o rapporto: ")
    unit_input = _text("Unità dell'angolo o del risultato (gradi/radianti): ").lower()
    units = {"gradi": "degrees", "radianti": "radians"}
    if unit_input not in units:
        raise ValueError("Unità non valida.")
    unit = units[unit_input]
    inverse_functions = {
        "asin": arithmetic.arcsine,
        "acos": arithmetic.arccosine,
        "atan": arithmetic.arctangent,
    }
    if name in functions:
        result = functions[name](value, unit)  # type: ignore[arg-type]
    elif name in inverse_functions:
        result = inverse_functions[name](value, unit)  # type: ignore[arg-type]
    else:
        sine = arithmetic.sine(value, unit)  # type: ignore[arg-type]
        cosine = arithmetic.cosine(value, unit)  # type: ignore[arg-type]
        if name == "sec":
            if math.isclose(cosine, 0.0, abs_tol=1e-12):
                raise ValueError("La secante non è definita per questo angolo.")
            result = 1 / cosine
        elif name == "cot":
            if math.isclose(sine, 0.0, abs_tol=1e-12):
                raise ValueError("La cotangente non è definita per questo angolo.")
            result = cosine / sine
        elif name == "csc":
            if math.isclose(sine, 0.0, abs_tol=1e-12):
                raise ValueError("La cosecante non è definita per questo angolo.")
            result = 1 / sine
        else:
            raise ValueError("Funzione non valida.")
    print(result)


def integration() -> None:
    expression = _text("Espressione: ")
    variables = _text("Variabili di integrazione (es. x oppure x,y,z): ").split(",")
    bounds: list[tuple[str, str, str]] = []
    definite = _text("Integrale definito? (si/no): ").lower() == "si"
    if definite:
        for variable in variables:
            bounds.append(
                (
                    variable.strip(),
                    _text(f"Limite inferiore di {variable}: "),
                    _text(f"Limite superiore di {variable}: "),
                )
            )
        print(multiple_integral(expression, bounds))
    elif len(variables) == 1:
        print(f"{integrate(expression, variables[0].strip())} + C")
    else:
        result = expression
        for variable in variables:
            result = integrate(result, variable.strip())
        print(f"{result} + C")


def differentiation() -> None:
    print(differentiate(_text("Espressione: "), _text("Variabile: "), _int("Ordine: ")))


def calculate_limit() -> None:
    print(
        limit(
            _text("Espressione: "),
            _text("Variabile: "),
            _text("Punto (es. 0, pi, oo): "),
            _text("Direzione (+, -, +-): "),
        )
    )


def equations() -> None:
    print(solve_equation(_text("Equazione (es. x^2 = 4): "), _text("Variabile: ")))


def expansion() -> None:
    print(expand(_text("Espressione da espandere: ")))


def number_theory() -> None:
    operation = _text("Operazione (fattoriale/mcd/mcm/fattori): ").lower()
    first = _int("Numero: ")
    if operation == "fattoriale":
        print(arithmetic.factorial(first))
    elif operation == "fattori":
        print(prime_factors(first))
    elif operation in {"mcd", "mcm"}:
        second = _int("Secondo numero: ")
        result = (
            arithmetic.gcd(first, second) if operation == "mcd" else arithmetic.lcm(first, second)
        )
        print(result)
    else:
        raise ValueError("Operazione non valida.")


def complex_number() -> None:
    print(complex(_float("Parte reale: "), _float("Parte immaginaria: ")))


def comparison() -> None:
    left = _float("Primo numero: ")
    right = _float("Secondo numero: ")
    print(f"{left} è {arithmetic.compare(left, right)} {right}")


def matrices() -> None:
    operation = _text("Operazione (mostra/determinante/inversa/prodotto): ").lower()
    matrix = parse_matrix(_text("Matrice, es. [[1,2],[3,4]]: "))
    if operation == "mostra":
        sp.pprint(matrix)
    elif operation == "determinante":
        print(determinant(matrix))
    elif operation == "inversa":
        sp.pprint(inverse(matrix))
    elif operation == "prodotto":
        sp.pprint(matrix_multiply(matrix, _text("Seconda matrice: ")))
    else:
        raise ValueError("Operazione non valida.")


def plotting() -> None:
    plot_expression(
        _text("Funzione: "),
        _text("Variabile: "),
        _float("Estremo sinistro: "),
        _float("Estremo destro: "),
    )


OPERATIONS: dict[str, tuple[str, Callable[[], None]]] = {
    "1": ("Aritmetica", arithmetic_menu),
    "2": ("Radici e logaritmi", roots_and_logs),
    "3": ("Trigonometria", trigonometry),
    "4": ("Integrali singoli, doppi e tripli", integration),
    "5": ("Derivate", differentiation),
    "6": ("Limiti", calculate_limit),
    "7": ("Equazioni", equations),
    "8": ("Espansione algebrica", expansion),
    "9": ("Teoria dei numeri", number_theory),
    "10": ("Numeri complessi", complex_number),
    "11": ("Confronto", comparison),
    "12": ("Matrici", matrices),
    "13": ("Grafico di una funzione", plotting),
}


def print_menu() -> None:
    print("\nCalcolatrice scientifica 2.0")
    for key, (label, _) in OPERATIONS.items():
        print(f"{key}. {label}")
    print("0. Esci")


def main() -> int:
    while True:
        print_menu()
        try:
            choice = input("Scelta: ").strip()
            if choice == "0":
                print("Arrivederci!")
                return 0
            if choice not in OPERATIONS:
                print("Scelta non valida. Riprova.")
                continue
            OPERATIONS[choice][1]()
        except (ValueError, ZeroDivisionError) as error:
            print(f"Errore: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nArrivederci!")
            return 0


if __name__ == "__main__":
    raise SystemExit(main())
