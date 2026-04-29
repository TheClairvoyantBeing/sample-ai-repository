# 🐍 Generative AI Engineering Program 🚀

Welcome to the **Generative AI Engineering Program** sample repository. This project is a carefully curated and sequential guide designed to take you from Python basics up to foundational Model Context Protocol (MCP) integrations and Data Science methodologies.

## 📚 Course Curriculum Layout

This repository has been structured sequentially. Progress from `01` to `06`.

1. **`01_python_basics/`**: Entry-level syntax, logic, and base semantics (Hello World, Loops, Conditionals).
2. **`02_python_intermediate/`**: Data structures, functions, modules, error handling, and file inputs/outputs.
3. **`03_python_advanced_ai/`**: Abstract Python configurations specifically intended for Artificial Intelligence/Machine Learning logic formatting.
4. **`04_data_science_fundamentals/`**: Working with matrices, dataframes, and plots utilizing `numpy`, `pandas`, and `matplotlib`.
5. **`05_model_context_protocol/`**: Learn how the MCP (Model Context Protocol) functions by bridging context to LLM connections.
6. **`06_projects_and_utils/`**: Applied examples, `conda` environment setups, and NLP sentiment-analysis systems.
7. **`07_flask_api_project/`**: Serving your Python AI application to real users over HTTP as a networked API!
8. **`08_machine_learning_modules/`**: Connecting standard algorithms via `sklearn` and interacting with external API endpoints.
9. **`09_chat_web_app/`**: A fully decoupled front-end GUI built with vanilla Web Technologies to interface with endpoints.

---

## 🗂️ Practice Data & Docs

- **`data/`**: `.csv` and `.txt` files containing practice tables simulating database exports. These are utilized by scripts within `02_python_intermediate`.
- **`docs/`**: Supplemental deep dives into python theory and generalized markdown basics.

---

## 🛠️ Getting Started

Follow the numerical directories in order. It is highly recommended to set up a virtual environment before diving into modules starting from level 04.

### 🔑 Environment Configuration
Modules 07, 08, and 09 require API keys and server configurations. 
1. Copy `.env.example` to `.env` in the root or module directory.
2. Fill in your `GROQ_API_KEY` (get one from [console.groq.com](https://console.groq.com/)).
3. Adjust other variables as needed.

**To run your first lesson:**
```bash
python 01_python_basics/01_hello_world.py
```

### Virtual Environments (Optional but Recommended)
Virtual environments keep your library dependencies scoped precisely to the application being run instead of polluting your system Python context.

**Windows:**
```powershell
python -m venv ai_env
ai_env\Scripts\activate
```

**macOS / Linux:**
```bash
python -m venv ai_env
source ai_env/bin/activate
```

Happy programming! 💻
