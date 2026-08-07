# Scientific Calculator 🧮

A Python scientific calculator featuring an interactive CLI, symbolic algebra,
multiple integrals, matrices, and function plotting. Version 2 separates the
mathematical engine from the user interface, making every operation reusable
and easy to test.

## Features

- Arithmetic with explicit error handling
- Roots and logarithms with domain validation
- Direct and inverse trigonometry in degrees or radians
- Indefinite and definite single, double, and triple integrals
- Symbolic bounds such as `pi`, `sqrt(2)`, and `oo`
- Arbitrary-order derivatives and directional limits
- Equation solving, including expressions such as `x^2 = 4`
- Algebraic expression expansion
- Factorials, GCD, LCM, and prime factorization
- Complex numbers
- Matrices, determinants, inverses, and multiplication
- Function plotting with configurable expressions and intervals

## Installation

Python 3.10 or later is required.

```bash
git clone https://github.com/JustCh3cco-19/sci-calculator.git
cd sci-calculator
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

To contribute, install the testing and linting tools as well:

```bash
python -m pip install -e ".[dev]"
```

## Usage

After installation, run:

```bash
sci-calculator
```

To run the project locally without installing the command:

```bash
python3 main.py
```

The package can also be launched directly:

```bash
python3 -m sci_calculator
```

Select `0` or press `Ctrl+C` to exit the CLI.

## Syntax and examples

Expressions follow SymPy syntax. Both `^` and `**` are accepted for
exponentiation.

| Operation | Example input | Result |
|---|---|---|
| Integral | `sin(x)`, from `0` to `pi` | `2` |
| Derivative | `x^3`, order `2` | `6*x` |
| Limit | `1/x`, point `oo` | `0` |
| Equation | `x^2 = 4` | `[-2, 2]` |
| Expansion | `(x+1)^2` | `x**2 + 2*x + 1` |
| Matrix | `[[1,2],[3,4]]` | 2×2 matrix |

The variables `x`, `y`, `z`, and `t` are supported, along with the constants
`pi`, `e`, and `oo`, and common functions such as `sin`, `cos`, `tan`, `sqrt`,
`log`, and `exp`.

### Library usage

```python
from sci_calculator import differentiate, integrate, solve_equation
from sci_calculator.matrices import determinant

print(integrate("sin(x)", lower="0", upper="pi"))
print(differentiate("x^3", order=2))
print(solve_equation("x^2 = 4"))
print(determinant("[[1, 2], [3, 4]]"))
```

## Project structure

```text
sci_calculator/
├── arithmetic.py   # Arithmetic, logarithms, and trigonometry
├── symbolic.py     # Symbolic algebra and calculus
├── matrices.py     # Matrix parsing and operations
├── plotting.py     # Matplotlib function plotting
└── cli.py          # Interactive command-line interface
main.py              # Local entry point
tests/               # Automated tests
```

## Testing and development

```bash
pytest
ruff check .
```

The test suite covers numerical operations, domain errors, symbolic calculus,
multiple integrals, equations, matrices, plotting, and essential CLI behavior.
GitHub Actions runs the tests and linter on Python 3.10 and Python 3.12.
