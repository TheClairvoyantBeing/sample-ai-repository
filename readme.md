# 🐍 Python Basics — A Learn-by-Doing Repository

A step-by-step Python course. Each file is a self-contained lesson —
open it, read the comments, run it, move on to the next.

## 📁 Repository Structure

```
sample-ai-repository/
├── lessons/          ← 15 numbered lesson files (start here)
├── data/             ← practice data files for lessons 14 & 15
├── docs/             ← learning-guide.md (detailed reference)
├── readme.md
└── sync.ps1          ← quick pull script
```

## 📚 Lessons

| #   | File                           | Topic                              |
| --- | ------------------------------ | ---------------------------------- |
| 01  | `01_hello_world.py`            | Your first program                 |
| 02  | `02_output.py`                 | print(), f-strings, sep & end      |
| 03  | `03_variables.py`              | Naming, assigning, type()          |
| 04  | `04_datatypes.py`              | str, int, float, bool              |
| 05  | `05_operators.py`              | Arithmetic, comparison, logical    |
| 06  | `06_user_input.py`             | input() and type conversion        |
| 07  | `07_conditional_statements.py` | if / elif / else / ternary         |
| 08  | `08_looping_statements.py`     | while, for, break, continue        |
| 09  | `09_functions.py`              | def, return, \*args, \*\*kwargs    |
| 10  | `10_data_structures.py`        | List, Tuple, Dictionary, Set       |
| 11  | `11_exception_handling.py`     | try / except / finally / raise     |
| 12  | `12_modules.py`                | datetime, os, math, random         |
| 13  | `13_mini_projects.py`          | ASCII bot + interactive calculator |
| 14  | `14_file_io.py`                | Read, write, append files          |
| 15  | `15_csv_operations.py`         | csv.reader / writer / DictReader   |

## 🗂️ Practice Data (`data/`)

| File               | Description                                            |
| ------------------ | ------------------------------------------------------ |
| `test.txt`         | Python article — string/file I/O exercises             |
| `students.csv`     | 15 students, 10 fields — filtering & sorting practice  |
| `db.csv`           | 12 user accounts, 12 fields — real-world data practice |
| `products.csv`     | 15 products, 10 fields — inventory/search practice     |
| `transactions.csv` | 20 bank transactions, 7 fields — financial analysis    |

## 🚀 Getting Started

```bash
# Run from the project root
python lessons/01_hello_world.py

# Pull latest changes from GitHub
.\sync.ps1
```

## 📖 Detailed Reference

See [`docs/learning-guide.md`](./docs/learning-guide.md) for full concept explanations and examples.
