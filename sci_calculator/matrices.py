"""Matrix parsing and common operations."""

from __future__ import annotations

import ast

import sympy as sp


def parse_matrix(value: str | list[list[object]]) -> sp.Matrix:
    if isinstance(value, str):
        try:
            value = ast.literal_eval(value)
        except (SyntaxError, ValueError) as error:
            raise ValueError("Usa il formato [[1, 2], [3, 4]].") from error
    if not isinstance(value, list) or not value or not all(isinstance(row, list) for row in value):
        raise ValueError("Una matrice deve essere una lista non vuota di righe.")
    if not value[0] or any(len(row) != len(value[0]) for row in value):
        raise ValueError("Tutte le righe devono avere la stessa lunghezza.")
    try:
        return sp.Matrix(value)
    except (TypeError, ValueError) as error:
        raise ValueError("La matrice contiene valori non validi.") from error


def determinant(matrix: str | list[list[object]] | sp.MatrixBase) -> sp.Expr:
    result = matrix if isinstance(matrix, sp.MatrixBase) else parse_matrix(matrix)
    if not result.is_square:
        raise ValueError("Il determinante richiede una matrice quadrata.")
    return result.det()


def inverse(matrix: str | list[list[object]] | sp.MatrixBase) -> sp.Matrix:
    result = matrix if isinstance(matrix, sp.MatrixBase) else parse_matrix(matrix)
    if not result.is_square:
        raise ValueError("L'inversa richiede una matrice quadrata.")
    if result.det() == 0:
        raise ValueError("La matrice è singolare e non ha inversa.")
    return result.inv()


def multiply(
    left: str | list[list[object]] | sp.MatrixBase,
    right: str | list[list[object]] | sp.MatrixBase,
) -> sp.Matrix:
    left_matrix = left if isinstance(left, sp.MatrixBase) else parse_matrix(left)
    right_matrix = right if isinstance(right, sp.MatrixBase) else parse_matrix(right)
    if left_matrix.cols != right_matrix.rows:
        raise ValueError("Le dimensioni delle matrici non sono compatibili.")
    return left_matrix * right_matrix
