# 🐍 Generative AI Engineering Program — Repository

A comprehensive repository for the **Generative AI Engineering Program** by [Campuspe](https://campuspe.com). Contains Python lessons, data science modules, MCP tutorials, projects, and weekly task reports.

## 📁 Repository Structure

```
sample-ai-repository/
├── lessons/              ← 18 numbered Python lesson files (start here)
├── data/                 ← practice data files for lessons 14 & 15
├── docs/                 ← learning-guide.md (detailed reference)
├── modules/              ← NumPy, Pandas, Matplotlib demos
├── mcp/                  ← Model Context Protocol tutorials (7 files)
├── projects/             ← sentiment-analysis, conda-envs
├── python-ai-context/    ← AI-focused Python utilities
├── markdown-basics/      ← Markdown syntax reference
├── weekly-reports/       ← Chapter 3: Weekly task reports (Weeks 1–6)
├── readme.md
└── sync.ps1              ← quick pull script
```

---

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
| 16  | `16_ai_context_datatypes.py`   | AI-focused data type usage         |
| 17  | `17_ai_context_loops.py`       | AI-focused loop patterns           |
| 18  | `18_ai_context_operators.py`   | AI-focused operator usage          |

## 📦 Modules

| Module     | File                    | Description                                 |
| ---------- | ----------------------- | ------------------------------------------- |
| NumPy      | `modules/numpy/`        | Array ops, reshaping, statistics for ML      |
| Pandas     | `modules/pandas/`       | DataFrame creation, filtering, value counts  |
| Matplotlib | `modules/matplotlib/`   | Loss & accuracy training visualization plots |

## 🔌 MCP (Model Context Protocol)

7 progressive tutorials in [`mcp/`](./mcp/) — from basics to a real-world example. See the [MCP README](./mcp/README.md).

## 🚀 Projects

| Project              | Path                           | Description                          |
| -------------------- | ------------------------------ | ------------------------------------ |
| Sentiment Analysis   | `projects/sentiment-analysis/` | HuggingFace Transformers pipeline    |
| Conda Environments   | `projects/conda-envs/`         | Example Conda env YAML configs       |

## 📝 Weekly Reports

Detailed weekly task reports for the program in [`weekly-reports/`](./weekly-reports/). Covers 6 weeks — from GenAI foundations to ML deployment.

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
