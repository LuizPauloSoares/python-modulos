# 🐍 Python Studies — Modules and Libraries

Repository dedicated to the practical study of **Python modules**: creating custom modules, using built-in modules, and integrating with external libraries.

---

## 📁 Project Structure

```
📦 estudos-python-modulos
 ┣ 📄 minha_calculadora.py      # Custom module with math operations
 ┣ 📄 teste_calculadora.py      # Import and test of the calculator module
 ┣ 📄 explorandoModuloOs.py     # Exploring the built-in `os` module
 ┗ 📄 moduloExterno.py          # HTTP request with the `requests` library
```

---

## 📌 File Descriptions

### `minha_calculadora.py`
Module built from scratch with the following math functions:

| Function | Description |
|---|---|
| `adicao(n1, n2)` | Returns the sum of two numbers |
| `subtracao(n1, n2)` | Returns the subtraction of two numbers |
| `multiplicacao(n1, n2)` | Returns the multiplication of two numbers |
| `divizao(n1, n2)` | Returns the division of two numbers |
| `restDivizao(n1, n2)` | Returns the remainder of the division (modulo `%`) |
| `divizaopor0(n1)` | Demonstrates a division-by-zero error |

---

### `teste_calculadora.py`
File that imports and uses the `minha_calculadora` module, testing the functions defined in it.

```python
import minha_calculadora

print(minha_calculadora.multiplicacao(7, 10))  # Output: 70
```

---

### `explorandoModuloOs.py`
Exploration of Python's built-in `os` module to interact with the operating system:

- `os.getcwd()` — gets the current directory
- `os.listdir()` — lists the files and folders in the directory
- `os.mkdir()` — creates new directories
- `os.environ` — accesses system environment variables

---

### `moduloExterno.py`
Use of the external `requests` library to make an HTTP request to the GitHub public API.

- Makes a `GET` call to `https://api.github.com`
- Handles status codes `200`, `404`, and others
- Uses a `try/except` block to catch exceptions

---

## 🚀 How to Run

**Prerequisite:** Python 3 installed.

1. Clone the repository:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Install the external dependency:
```bash
pip install requests
```

3. Run the scripts individually:
```bash
python teste_calculadora.py
python explorandoModuloOs.py
python moduloExterno.py
```

---

## 🧠 Concepts
