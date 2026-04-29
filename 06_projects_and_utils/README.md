# 🚀 06 - Projects, Envs, and Utilities

A collection of applied projects, configurations, and scripts to demonstrate end-to-end Python concepts.

## 📁 Contents

### 1. `01_ascii_bot.py`
An interactive terminal bot calculator putting basic Python concepts to work. It demonstrates:
- Command-line interaction and parsing
- Basic control flow and operations
- Taking user input and generating formatted output

**To run:**
```bash
python 01_ascii_bot.py
```

### 2. `02_sentiment_analysis/`
A practical application utilizing a pre-trained NLP pipeline from HuggingFace's `transformers` library.
It covers:
- Setting up a virtual environment and installing dependencies
- Downloading and initializing a pre-trained sentiment analysis model
- Running text classification (Positive/Negative sentiment)

**To run:**
```bash
cd 02_sentiment_analysis
pip install -r requirements.txt
python sentiment_analyzer.py
```

### 3. `03_utils/`
Helpful functional Python utility scripts containing helper functions that can be imported and reused across different projects. This section illustrates code modularity and Python module imports.

### 4. `04_conda_envs/`
Example environment YAML descriptors for setting up Data Science and NLP environments using Conda. These files (`.yml`) specify the python version and the required packages to establish reproducible environments.

**To use:**
```bash
cd 04_conda_envs
conda env create -f environment.yml
```
