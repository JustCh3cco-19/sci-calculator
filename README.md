# Scientific Calculator 🧮

> **Advanced CLI-based scientific calculator written in Python. Supports symbolic computation, plotting, integrals, and matrix operations.**

This is a full-featured Python scientific calculator project with:
- a text-based interactive CLI,
- support for symbolic algebra (via `sympy`),
- definite/infinite integrals,
- trigonometry and logarithms,
- matrix and complex number handling.

---

## ✨ Features

- ✅ Basic arithmetic: `+`, `-`, `×`, `÷`, `^`
- 🔁 Loops through calculations in a CLI
- 📐 Trigonometric functions (`sin`, `cos`, `tan`, etc.)
- 🔢 Logarithms and roots
- 📈 Plotting (Matplotlib)
- 📚 Symbolic math (SymPy)
- 🧮 Definite & indefinite integrals (1D/2D/3D)
- 📏 Derivatives & limits
- 📊 Matrices and complex numbers
- 🎯 Equation solving

---

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/JustCh3cco-19/sci-calculator.git
cd sci-calculator
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install sympy mpmath numpy matplotlib
```

---

## 🚀 Usage

You can launch each script depending on the topic:

```bash
python calcolatrice.py           # Full CLI calculator
python integrals.py              # 1D definite/indefinite integrals
python defined_integrals.py      # 2D and 3D definite integrals
```

---

## 📂 File Overview

- `calcolatrice.py` – main interactive CLI calculator
- `integrals.py` – basic 1D integral handling
- `defined_integrals.py` – 2D/3D definite integral calculator

---

## 🔧 Tech Stack

- Python 3
- SymPy
- NumPy
- Matplotlib
- Mpmath

---

## 📌 Notes

- All math is handled symbolically using `sympy` for precision
- The CLI provides an educational interface for learning math operations
- Integrals and limits support symbolic boundaries
