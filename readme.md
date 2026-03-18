# 🐍 Generative AI Engineering Program — Repository

A comprehensive repository for the **Generative AI Engineering Program** by [Campuspe](https://campuspe.com). Contains Program Curriculum (Python, Data Science, MCP), data files, project environments, and specialized utilities.

## 📁 Repository Structure

```
sample-ai-repository/
├── core/                 ← Program Curriculum
│   ├── python/           ← 18 numbered Python lesson files
│   ├── data-science/     ← NumPy, Pandas, Matplotlib demos
│   ├── mcp/              ← Model Context Protocol tutorials
│   └── markdown/         ← Markdown syntax reference
├── data/                 ← practice data files for lessons
├── docs/                 ← learning-guide.md (detailed reference)
├── projects/             ← sentiment-analysis, conda-envs
├── utils/                ← AI-focused Python utilities (functions.py)
├── readme.md
└── sync.ps1              ← quick pull script
```

---

## 📚 Lessons

| #   | File                               | Topic                              |
| --- | ---------------------------------- | ---------------------------------- |
| 01  | `core/python/01_hello_world.py`    | Your first program                 |
| 02  | `core/python/02_output.py`         | print(), f-strings, sep & end      |
| 03  | `core/python/03_variables.py`      | Naming, assigning, type()          |
| 04  | `core/python/04_datatypes.py`      | str, int, float, bool              |
| 05  | `core/python/05_operators.py`      | Arithmetic, comparison, logical    |
| 06  | `core/python/06_user_input.py`     | input() and type conversion        |
| 07  | `core/python/07_conditional.py`    | if / elif / else / ternary         |
| 08  | `core/python/08_looping.py`        | while, for, break, continue        |
| 09  | `core/python/09_functions.py`      | def, return, *args, **kwargs       |
| 10  | `core/python/10_structures.py`     | List, Tuple, Dictionary, Set       |
| 11  | `core/python/11_exceptions.py`     | try / except / finally / raise     |
| 12  | `core/python/12_modules.py`        | datetime, os, math, random         |
| 13  | `core/python/13_projects.py`       | ASCII bot + interactive calculator |
| 14  | `core/python/14_file_io.py`        | Read, write, append files          |
| 15  | `core/python/15_csv_ops.py`        | csv.reader / writer / DictReader   |
| 16  | `core/python/16_ai_datatypes.py`   | AI-focused data type usage         |
| 17  | `core/python/17_ai_loops.py`       | AI-focused loop patterns           |
| 18  | `core/python/18_ai_operators.py`   | AI-focused operator usage          |

## 📦 Modules

| Module     | Path                           | Description                                 |
| ---------- | ------------------------------ | ------------------------------------------- |
| NumPy      | `core/data-science/numpy/`     | Array ops, reshaping, statistics for ML      |
| Pandas     | `core/data-science/pandas/`    | DataFrame creation, filtering, value counts  |
| Matplotlib | `core/data-science/matplotlib/`| Loss & accuracy training visualization plots |

## 🔌 MCP (Model Context Protocol)

7 progressive tutorials in [`core/mcp/`](./core/mcp/) — from basics to a real-world example. See the [MCP README](./core/mcp/README.md).

## 🚀 Projects

| Project              | Path                           | Description                          |
| -------------------- | ------------------------------ | ------------------------------------ |
| Sentiment Analysis   | `projects/sentiment-analysis/` | HuggingFace Transformers pipeline    |
| Conda Environments   | `projects/conda-envs/`         | Example Conda env YAML configs       |


## 🗂️ Practice Data (`data/`)

| File               | Description                                            |
| ------------------ | ------------------------------------------------------ |
| `test.txt`         | Python article — string/file I/O exercises             |
| `students.csv`     | 15 students, 10 fields — filtering & sorting practice  |
| `db.csv`           | 12 user accounts, 12 fields — real-world data practice |
| `products.csv`     | 15 products, 10 fields — inventory/search practice     |
| `transactions.csv` | 20 bank transactions, 7 fields — financial analysis    |

---

## 🛠️ Getting Started

```bash
# Run from the project root
python lessons/01_hello_world.py

# Pull latest changes from GitHub
.\sync.ps1
```

## 📖 Detailed Reference

See [`docs/learning-guide.md`](./docs/learning-guide.md) for full concept explanations and examples.

---

## 🖥️ Virtual Environment Setup

### What is a Virtual Environment?

An isolated Python environment that lets you:

- Install project-specific packages without affecting other projects
- Use different package versions for different projects
- Avoid dependency conflicts
- Keep project coordination clean

```
Project A -> venv_a -> TensorFlow 2.10
Project B -> venv_b -> TensorFlow 2.12
```

### Commands

**Windows:**
```powershell
cd project-name
python -m venv <env-name>
<env-name>\Scripts\activate
deactivate
```

**macOS / Linux:**
```bash
cd project-name
python -m venv <env-name>
source <env-name>/bin/activate
deactivate
```
