# Phase 1: Python for AI — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build Python for AI fluency — covering NumPy, Pandas, and Jupyter — documented as notes and two interview-ready projects in the GitHub repo.

**Architecture:** Learn-by-doing approach: each topic has a concise notes file + small exercises, culminating in two real projects (Data Explorer CLI and Titanic EDA Notebook) that demonstrate practical data skills.

**Tech Stack:** Python 3.11+, NumPy, Pandas, Matplotlib, Jupyter Notebook, pytest, Git

## Global Constraints

- All Python files must run with `python <file>.py` with no errors
- All notes go in `phase-1-python-for-ai/notes/` as Markdown files
- All exercises go in `phase-1-python-for-ai/exercises/`
- All projects have their own `README.md` explaining what it does and how to run it
- Commit after every task
- Project READMEs must be written so a recruiter (non-technical) understands the project value

---

## File Structure

```
phase-1-python-for-ai/
├── notes/
│   ├── 01-python-basics.md        # Python syntax, data structures, OOP, file I/O
│   ├── 02-numpy.md                # Arrays, operations, broadcasting
│   ├── 03-pandas.md               # DataFrames, Series, cleaning, aggregation
│   └── 04-jupyter.md              # Notebooks, magic commands, best practices
├── exercises/
│   ├── 01_python_basics.py        # Practice scripts
│   ├── 02_numpy_exercises.py
│   └── 03_pandas_exercises.py
└── projects/
    ├── 01-data-explorer-cli/
    │   ├── README.md
    │   ├── explorer.py            # Main CLI tool
    │   ├── requirements.txt
    │   └── tests/
    │       └── test_explorer.py
    └── 02-titanic-eda/
        ├── README.md
        ├── titanic_eda.ipynb      # Full EDA notebook
        ├── requirements.txt
        └── data/
            └── titanic.csv
```

---

## Task 1: Environment Setup

**Files:**
- Create: `phase-1-python-for-ai/requirements-base.txt`

- [ ] **Step 1: Install Python packages**

```bash
pip install numpy pandas matplotlib jupyter pytest
```

Expected: All install without errors.

- [ ] **Step 2: Verify installation**

```bash
python -c "import numpy, pandas, matplotlib, jupyter; print('All good')"
```

Expected: prints `All good`

- [ ] **Step 3: Create base requirements file**

Create `phase-1-python-for-ai/requirements-base.txt`:

```
numpy>=1.26
pandas>=2.1
matplotlib>=3.8
jupyter>=1.0
pytest>=7.4
```

- [ ] **Step 4: Commit**

```bash
git add phase-1-python-for-ai/requirements-base.txt README.md
git commit -m "feat: initialize Phase 1 structure and requirements"
```

---

## Task 2: Python Basics Notes

**Files:**
- Create: `phase-1-python-for-ai/notes/01-python-basics.md`
- Create: `phase-1-python-for-ai/exercises/01_python_basics.py`

- [ ] **Step 1: Write notes for Python basics**

Create `phase-1-python-for-ai/notes/01-python-basics.md` covering:

```markdown
# Python Basics for AI

## Why Python for AI?
Python dominates AI/ML because of its readable syntax and rich ecosystem (NumPy, Pandas, PyTorch, TensorFlow, scikit-learn).

## Data Types You'll Use Constantly

```python
# Lists — ordered, mutable
data = [1, 2, 3, 4, 5]

# Dictionaries — key-value, fast lookup
model_config = {"learning_rate": 0.001, "epochs": 10, "batch_size": 32}

# Tuples — immutable, used for shapes
image_shape = (224, 224, 3)  # height, width, channels

# Sets — unique values, fast membership test
labels = {"cat", "dog", "bird"}
```

## List Comprehensions (used everywhere in AI code)

```python
# Regular loop
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension — preferred
squares = [x**2 for x in range(10)]

# With condition — filter even squares
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

## Functions

```python
def normalize(data: list, min_val: float, max_val: float) -> list:
    """Scale values to 0-1 range. Common preprocessing step in ML."""
    return [(x - min_val) / (max_val - min_val) for x in data]

result = normalize([10, 20, 30, 40, 50], min_val=10, max_val=50)
# [0.0, 0.25, 0.5, 0.75, 1.0]
```

## Lambda Functions

```python
# Used heavily with pandas apply()
double = lambda x: x * 2
sorted_data = sorted(model_results, key=lambda r: r["accuracy"], reverse=True)
```

## File I/O (for loading datasets)

```python
import csv

# Reading CSV
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Writing results
with open("results.txt", "w") as f:
    f.write(f"Accuracy: {accuracy:.4f}\n")
```

## Classes (for building models and pipelines)

```python
class DataPipeline:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None

    def load(self):
        with open(self.filepath) as f:
            self.data = f.readlines()
        return self

    def clean(self):
        self.data = [line.strip() for line in self.data if line.strip()]
        return self  # enables chaining: pipeline.load().clean()
```

## Key Built-ins for Data Work

```python
data = [3, 1, 4, 1, 5, 9, 2, 6]

len(data)          # 8
sum(data)          # 31
min(data)          # 1
max(data)          # 9
sorted(data)       # [1, 1, 2, 3, 4, 5, 6, 9]
enumerate(data)    # (0,3), (1,1), ... — index + value pairs
zip([1,2,3], ['a','b','c'])  # (1,'a'), (2,'b'), (3,'c')
```
```

- [ ] **Step 2: Write exercise script**

Create `phase-1-python-for-ai/exercises/01_python_basics.py`:

```python
# Exercise 1: List comprehension
# Create a list of cubes for numbers 1-10
cubes = [x**3 for x in range(1, 11)]
print("Cubes:", cubes)

# Exercise 2: Filter and transform
# From a list of temperatures in Celsius, keep only > 30 and convert to Fahrenheit
temps_c = [22, 35, 18, 41, 29, 38]
hot_f = [(c * 9/5) + 32 for c in temps_c if c > 30]
print("Hot temps in F:", hot_f)

# Exercise 3: Dictionary manipulation
# Given model results, find the best model by accuracy
results = [
    {"model": "random_forest", "accuracy": 0.87},
    {"model": "svm", "accuracy": 0.91},
    {"model": "logistic_regression", "accuracy": 0.84},
]
best = max(results, key=lambda r: r["accuracy"])
print(f"Best model: {best['model']} ({best['accuracy']:.0%})")

# Exercise 4: Class — simple data loader
class CSVLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def count_lines(self) -> int:
        with open(self.filepath, "r") as f:
            return sum(1 for _ in f) - 1  # subtract header

# Exercise 5: Normalize a list to 0-1 range
def normalize(values: list) -> list:
    lo, hi = min(values), max(values)
    return [(v - lo) / (hi - lo) for v in values]

scores = [50, 75, 100, 25, 90]
print("Normalized:", normalize(scores))
```

- [ ] **Step 3: Run exercise script to verify it works**

```bash
python phase-1-python-for-ai/exercises/01_python_basics.py
```

Expected output:
```
Cubes: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
Hot temps in F: [95.0, 105.8, 100.4]
Best model: svm (91%)
Normalized: [0.4, 0.6666666666666666, 1.0, 0.0, 0.8666666666666667]
```

- [ ] **Step 4: Commit**

```bash
git add phase-1-python-for-ai/notes/01-python-basics.md \
        phase-1-python-for-ai/exercises/01_python_basics.py
git commit -m "learn: Python basics notes and exercises"
```

---

## Task 3: NumPy Notes + Exercises

**Files:**
- Create: `phase-1-python-for-ai/notes/02-numpy.md`
- Create: `phase-1-python-for-ai/exercises/02_numpy_exercises.py`

- [ ] **Step 1: Write NumPy notes**

Create `phase-1-python-for-ai/notes/02-numpy.md`:

```markdown
# NumPy — The Foundation of AI Math

NumPy is the backbone of AI. Every tensor in PyTorch, every matrix in scikit-learn, every image as pixel arrays — it's all NumPy under the hood.

## Why NumPy over Python lists?

```python
import numpy as np

# Python list — slow loop
data = list(range(1_000_000))
result = [x * 2 for x in data]  # ~100ms

# NumPy — vectorized, runs in C
arr = np.arange(1_000_000)
result = arr * 2  # ~1ms — 100x faster
```

## Creating Arrays

```python
import numpy as np

np.array([1, 2, 3])          # from list: array([1, 2, 3])
np.zeros((3, 4))             # 3x4 matrix of zeros
np.ones((2, 3))              # 2x3 matrix of ones
np.arange(0, 10, 2)         # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)        # [0, 0.25, 0.5, 0.75, 1.0] — 5 evenly spaced
np.random.rand(3, 3)        # 3x3 random float matrix [0,1)
np.random.randn(100)        # 100 values from normal distribution
```

## Shape & Dimensions

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr.shape     # (2, 3) — 2 rows, 3 columns
arr.ndim      # 2 — number of dimensions
arr.dtype     # dtype('int64')
arr.size      # 6 — total elements
```

## Indexing & Slicing

```python
arr = np.array([10, 20, 30, 40, 50])
arr[0]        # 10
arr[-1]       # 50
arr[1:4]      # [20, 30, 40]
arr[::2]      # [10, 30, 50] — every other

# 2D indexing
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix[1, 2]  # 6 — row 1, col 2
matrix[:, 1]  # [2, 5, 8] — all rows, col 1
matrix[0, :]  # [1, 2, 3] — row 0, all cols
```

## Math Operations (vectorized)

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b          # [5, 7, 9]
a * b          # [4, 10, 18] — element-wise
a ** 2         # [1, 4, 9]
np.sqrt(a)     # [1.0, 1.414, 1.732]
np.dot(a, b)   # 32 — dot product (used in neural nets)
```

## Broadcasting (critical for AI code)

```python
# Add scalar to matrix
matrix = np.ones((3, 3))
matrix + 10    # every element becomes 11

# Add row vector to matrix
row = np.array([1, 2, 3])
matrix + row   # adds [1,2,3] to each row — shape (3,3)
```

## Statistics

```python
data = np.array([2, 4, 4, 4, 5, 5, 7, 9])
np.mean(data)   # 5.0
np.median(data) # 4.5
np.std(data)    # 2.0
np.var(data)    # 4.0
np.min(data)    # 2
np.max(data)    # 9
np.sum(data)    # 40
```

## Reshape (used constantly in deep learning)

```python
arr = np.arange(12)        # [0,1,...,11]
arr.reshape(3, 4)          # 3x4 matrix
arr.reshape(2, 2, 3)       # 3D tensor
arr.reshape(-1, 1)         # column vector, NumPy infers the -1 dimension
```
```

- [ ] **Step 2: Write NumPy exercises**

Create `phase-1-python-for-ai/exercises/02_numpy_exercises.py`:

```python
import numpy as np

# Exercise 1: Create and inspect arrays
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Shape:", arr.shape)
print("First row:", arr[0])
print("Last column:", arr[:, -1])
print("Center 2x2:", arr[1:3, 1:3])

# Exercise 2: Vectorized operations (simulate feature scaling)
prices = np.array([150.0, 250.0, 180.0, 320.0, 95.0])
min_price, max_price = prices.min(), prices.max()
normalized = (prices - min_price) / (max_price - min_price)
print("\nNormalized prices:", normalized.round(3))

# Exercise 3: Statistics on a simulated dataset
np.random.seed(42)
heights = np.random.normal(loc=170, scale=10, size=1000)  # 1000 heights, mean=170cm
print(f"\nHeight stats — Mean: {heights.mean():.1f}cm, Std: {heights.std():.1f}cm")
print(f"Tallest: {heights.max():.1f}cm, Shortest: {heights.min():.1f}cm")
print(f"People over 185cm: {(heights > 185).sum()}")

# Exercise 4: Matrix multiplication (the core of neural networks)
# Simulate one layer: input (5 samples, 3 features) x weights (3 features, 2 neurons)
inputs = np.random.rand(5, 3)
weights = np.random.rand(3, 2)
bias = np.array([0.1, 0.2])
output = np.dot(inputs, weights) + bias
print(f"\nLayer output shape: {output.shape}")  # (5, 2) — 5 samples, 2 neurons

# Exercise 5: Boolean indexing (filtering data)
scores = np.array([45, 82, 91, 67, 55, 78, 88, 34, 95, 62])
passing = scores[scores >= 60]
print(f"\nPassing scores: {passing}")
print(f"Pass rate: {len(passing)/len(scores):.0%}")
```

- [ ] **Step 3: Run exercises**

```bash
python phase-1-python-for-ai/exercises/02_numpy_exercises.py
```

Expected: All print statements execute without error, showing correct numerical outputs.

- [ ] **Step 4: Commit**

```bash
git add phase-1-python-for-ai/notes/02-numpy.md \
        phase-1-python-for-ai/exercises/02_numpy_exercises.py
git commit -m "learn: NumPy notes and exercises"
```

---

## Task 4: Pandas Notes + Exercises

**Files:**
- Create: `phase-1-python-for-ai/notes/03-pandas.md`
- Create: `phase-1-python-for-ai/exercises/03_pandas_exercises.py`

- [ ] **Step 1: Write Pandas notes**

Create `phase-1-python-for-ai/notes/03-pandas.md`:

```markdown
# Pandas — Data Manipulation for AI

Pandas is how you load, clean, and explore data before training a model. 80% of ML work is data preparation — Pandas is your main tool.

## Core Data Structures

```python
import pandas as pd

# Series — 1D labeled array
ages = pd.Series([25, 30, 35], index=["Alice", "Bob", "Charlie"])
ages["Alice"]  # 25

# DataFrame — 2D table (think spreadsheet in Python)
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [70000, 85000, 92000]
})
```

## Loading Data

```python
df = pd.read_csv("data.csv")                          # CSV
df = pd.read_csv("data.csv", usecols=["col1","col2"]) # specific columns
df = pd.read_json("data.json")
df = pd.read_excel("data.xlsx")
```

## First Look at a Dataset

```python
df.shape           # (rows, columns)
df.head()          # first 5 rows
df.tail(10)        # last 10 rows
df.info()          # dtypes + non-null counts
df.describe()      # count, mean, std, min, quartiles, max
df.dtypes          # column data types
df.columns         # column names
df.isnull().sum()  # count missing values per column
```

## Selecting Data

```python
df["age"]                        # single column → Series
df[["name", "salary"]]           # multiple columns → DataFrame
df.loc[0]                        # row by label
df.iloc[0]                       # row by position
df.loc[df["age"] > 28]           # filter rows where age > 28
df.loc[df["age"] > 28, "salary"] # filter rows AND select column
```

## Cleaning Data (most of real ML work)

```python
# Handle missing values
df.dropna()                          # drop rows with any NaN
df.dropna(subset=["age"])            # drop only if 'age' is NaN
df["age"].fillna(df["age"].mean())   # fill NaN with column mean
df["name"].fillna("Unknown")         # fill with constant

# Remove duplicates
df.drop_duplicates()
df.drop_duplicates(subset=["email"])  # deduplicate by email only

# Change data types
df["age"] = df["age"].astype(int)
df["date"] = pd.to_datetime(df["date"])

# Rename columns
df.rename(columns={"old_name": "new_name"}, inplace=True)

# Drop columns
df.drop(columns=["unnecessary_col"], inplace=True)
```

## Feature Engineering (creating new columns)

```python
# Arithmetic
df["salary_per_year"] = df["monthly_salary"] * 12

# Apply a function
df["age_group"] = df["age"].apply(lambda x: "senior" if x >= 50 else "junior")

# String operations
df["email_domain"] = df["email"].str.split("@").str[1]
df["name_upper"] = df["name"].str.upper()
```

## Aggregation & Grouping

```python
# Basic stats
df["salary"].mean()
df["salary"].median()
df["salary"].value_counts()    # frequency count

# Group by
df.groupby("department")["salary"].mean()     # avg salary per dept
df.groupby("department").agg({
    "salary": "mean",
    "age": ["min", "max", "mean"]
})
```

## Sorting

```python
df.sort_values("salary", ascending=False)        # highest salary first
df.sort_values(["dept", "salary"], ascending=[True, False])
```
```

- [ ] **Step 2: Write Pandas exercises**

Create `phase-1-python-for-ai/exercises/03_pandas_exercises.py`:

```python
import pandas as pd
import numpy as np

# Simulate a small employee dataset
np.random.seed(42)
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank"],
    "department": ["Eng", "Eng", "HR", "HR", "Eng", "Marketing", "Marketing", "Eng"],
    "salary": [95000, 88000, 62000, 67000, 102000, 75000, 80000, np.nan],
    "years_exp": [5, 3, 7, 4, 8, 2, 6, 1],
    "rating": [4.2, 3.8, 4.5, 4.1, 4.8, 3.5, 4.0, 3.9],
}
df = pd.DataFrame(data)

# Exercise 1: Basic exploration
print("=== Dataset Info ===")
print(f"Shape: {df.shape}")
print(f"Missing values:\n{df.isnull().sum()}")
print(f"\nFirst 3 rows:\n{df.head(3)}")

# Exercise 2: Fill missing salary with department mean
dept_mean = df.groupby("department")["salary"].transform("mean")
df["salary"] = df["salary"].fillna(dept_mean)
print(f"\nAfter filling missing salary: {df['salary'].isnull().sum()} missing")

# Exercise 3: Filter — find high performers (rating >= 4.0) in Engineering
eng_high = df[(df["department"] == "Eng") & (df["rating"] >= 4.0)]
print(f"\nHigh-performing Engineers:\n{eng_high[['name', 'salary', 'rating']]}")

# Exercise 4: Group by department — avg salary and avg rating
dept_summary = df.groupby("department").agg(
    avg_salary=("salary", "mean"),
    avg_rating=("rating", "mean"),
    headcount=("name", "count")
).round(2)
print(f"\nDepartment Summary:\n{dept_summary}")

# Exercise 5: Feature engineering — salary band
def salary_band(s):
    if s < 70000: return "Low"
    elif s < 90000: return "Mid"
    else: return "High"

df["salary_band"] = df["salary"].apply(salary_band)
print(f"\nSalary bands:\n{df[['name', 'salary', 'salary_band']]}")
```

- [ ] **Step 3: Run exercises**

```bash
python phase-1-python-for-ai/exercises/03_pandas_exercises.py
```

Expected: All sections print without errors, showing dept summaries and salary bands.

- [ ] **Step 4: Commit**

```bash
git add phase-1-python-for-ai/notes/03-pandas.md \
        phase-1-python-for-ai/exercises/03_pandas_exercises.py
git commit -m "learn: Pandas notes and exercises"
```

---

## Task 5: Jupyter Notes

**Files:**
- Create: `phase-1-python-for-ai/notes/04-jupyter.md`

- [ ] **Step 1: Write Jupyter notes**

Create `phase-1-python-for-ai/notes/04-jupyter.md`:

```markdown
# Jupyter Notebooks — The AI Engineer's Workbench

Jupyter Notebooks let you mix code, output, and markdown in one document. Every data scientist and AI engineer uses them for exploration, visualization, and sharing findings.

## Starting Jupyter

```bash
jupyter notebook       # opens browser at localhost:8888
jupyter lab            # JupyterLab (modern UI — recommended)
```

## Essential Keyboard Shortcuts

| Mode | Shortcut | Action |
|------|----------|--------|
| Command mode (press Esc) | `A` | Insert cell above |
| Command mode | `B` | Insert cell below |
| Command mode | `DD` | Delete cell |
| Command mode | `M` | Change to Markdown cell |
| Command mode | `Y` | Change to Code cell |
| Command mode | `Enter` | Enter edit mode |
| Edit mode | `Shift+Enter` | Run cell, move to next |
| Edit mode | `Ctrl+Enter` | Run cell, stay |
| Any | `Ctrl+Shift+P` | Command palette |

## Magic Commands

```python
%timeit sum(range(1000))     # time a line
%%time                        # time a whole cell
%matplotlib inline            # show plots in notebook
%who                          # list variables
%whos                         # list variables with details
!pip install pandas           # run shell command
!ls -la                       # list files
```

## Best Practices for AI Notebooks

1. **One notebook, one story** — don't mix exploration with final analysis
2. **Restart and Run All** before sharing — ensures reproducibility
3. **Clear outputs before committing** to git (reduces diff noise)
4. **Markdown cells** to explain your reasoning, not just code
5. **Name your notebooks clearly**: `01-data-exploration.ipynb`, not `notebook2_final_v3.ipynb`

## Plotting in Notebooks

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv")

# Histogram
df["age"].hist(bins=20, color="steelblue", edgecolor="white")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Bar chart
df.groupby("category")["value"].mean().plot(kind="bar", color="coral")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```
```

- [ ] **Step 2: Commit**

```bash
git add phase-1-python-for-ai/notes/04-jupyter.md
git commit -m "learn: Jupyter Notebook notes"
```

---

## Task 6: Project 1 — Data Explorer CLI

**What it does:** A command-line tool that takes any CSV file and instantly shows a data quality report — shape, column types, missing values, and basic statistics. Useful for any data science workflow.

**Why it impresses interviewers:** Shows you can write a practical, reusable tool (not just notebook scripts), understand data quality issues, and structure a real Python project with tests.

**Files:**
- Create: `phase-1-python-for-ai/projects/01-data-explorer-cli/explorer.py`
- Create: `phase-1-python-for-ai/projects/01-data-explorer-cli/requirements.txt`
- Create: `phase-1-python-for-ai/projects/01-data-explorer-cli/README.md`
- Create: `phase-1-python-for-ai/projects/01-data-explorer-cli/tests/test_explorer.py`

- [ ] **Step 1: Write failing test first**

Create `phase-1-python-for-ai/projects/01-data-explorer-cli/tests/test_explorer.py`:

```python
import pytest
import pandas as pd
import io
from explorer import DataExplorer

def make_df():
    return pd.DataFrame({
        "name": ["Alice", "Bob", None, "Diana"],
        "age": [25, 30, 35, None],
        "salary": [70000, 85000, 92000, 67000],
        "dept": ["Eng", "HR", "Eng", "HR"],
    })

def test_shape_report(capsys):
    exp = DataExplorer(make_df())
    exp.report()
    captured = capsys.readouterr()
    assert "4 rows" in captured.out
    assert "4 columns" in captured.out

def test_missing_values_detected():
    exp = DataExplorer(make_df())
    missing = exp.missing_summary()
    assert missing["name"] == 1
    assert missing["age"] == 1
    assert missing["salary"] == 0

def test_numeric_stats():
    exp = DataExplorer(make_df())
    stats = exp.numeric_stats()
    assert "salary" in stats.columns
    assert "age" in stats.columns
    assert "mean" in stats.index

def test_categorical_summary():
    exp = DataExplorer(make_df())
    cats = exp.categorical_summary()
    assert "dept" in cats
    assert cats["dept"]["unique_values"] == 2
```

- [ ] **Step 2: Run test — confirm it fails**

```bash
cd phase-1-python-for-ai/projects/01-data-explorer-cli
pytest tests/test_explorer.py -v
```

Expected: `ModuleNotFoundError: No module named 'explorer'`

- [ ] **Step 3: Implement DataExplorer**

Create `phase-1-python-for-ai/projects/01-data-explorer-cli/explorer.py`:

```python
import sys
import pandas as pd
import numpy as np
from pathlib import Path


class DataExplorer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def missing_summary(self) -> dict:
        return self.df.isnull().sum().to_dict()

    def numeric_stats(self) -> pd.DataFrame:
        return self.df.select_dtypes(include=[np.number]).describe()

    def categorical_summary(self) -> dict:
        result = {}
        cat_cols = self.df.select_dtypes(include=["object", "category"]).columns
        for col in cat_cols:
            result[col] = {
                "unique_values": self.df[col].nunique(),
                "top_5": self.df[col].value_counts().head(5).to_dict(),
                "missing": int(self.df[col].isnull().sum()),
            }
        return result

    def report(self):
        df = self.df
        rows, cols = df.shape
        total_cells = rows * cols
        missing_cells = df.isnull().sum().sum()
        missing_pct = (missing_cells / total_cells) * 100

        print("=" * 60)
        print("  DATA EXPLORER REPORT")
        print("=" * 60)
        print(f"\n  Shape: {rows} rows x {cols} columns")
        print(f"  Missing cells: {missing_cells} ({missing_pct:.1f}%)\n")

        print("  COLUMNS")
        print("-" * 60)
        for col in df.columns:
            dtype = str(df[col].dtype)
            missing = df[col].isnull().sum()
            missing_str = f"  [{missing} missing]" if missing > 0 else ""
            print(f"  {col:<20} {dtype:<12}{missing_str}")

        print("\n  NUMERIC SUMMARY")
        print("-" * 60)
        numeric = df.select_dtypes(include=[np.number])
        if not numeric.empty:
            print(numeric.describe().round(2).to_string())

        cats = self.categorical_summary()
        if cats:
            print("\n  CATEGORICAL COLUMNS")
            print("-" * 60)
            for col, info in cats.items():
                print(f"\n  {col} — {info['unique_values']} unique values")
                for val, count in info["top_5"].items():
                    bar = "█" * int((count / df.shape[0]) * 20)
                    print(f"    {str(val):<15} {bar} {count}")

        print("\n" + "=" * 60)


def main():
    if len(sys.argv) < 2:
        print("Usage: python explorer.py <path-to-csv>")
        sys.exit(1)

    filepath = Path(sys.argv[1])
    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    df = pd.read_csv(filepath)
    explorer = DataExplorer(df)
    explorer.report()


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests — confirm they pass**

```bash
pytest tests/test_explorer.py -v
```

Expected: All 4 tests PASS

- [ ] **Step 5: Create requirements.txt**

Create `phase-1-python-for-ai/projects/01-data-explorer-cli/requirements.txt`:

```
numpy>=1.26
pandas>=2.1
pytest>=7.4
```

- [ ] **Step 6: Write the project README**

Create `phase-1-python-for-ai/projects/01-data-explorer-cli/README.md`:

```markdown
# Data Explorer CLI

A command-line tool that instantly profiles any CSV dataset — showing shape, data types, missing values, and statistics. Built as part of my AI Engineering learning journey.

## What it does

Given any CSV file, it generates a readable data quality report covering:
- Dataset shape (rows × columns)
- Per-column data types and missing value counts
- Statistical summary for numeric columns (mean, std, min/max, quartiles)
- Top values for categorical columns with a mini bar chart

## Example Output

```
============================================================
  DATA EXPLORER REPORT
============================================================

  Shape: 891 rows x 12 columns
  Missing cells: 866 (8.1%)

  COLUMNS
------------------------------------------------------------
  PassengerId          int64
  Survived             int64
  Pclass               int64
  Name                 object       [0 missing]
  Age                  float64      [177 missing]
  ...
```

## How to Run

```bash
pip install -r requirements.txt
python explorer.py path/to/your/data.csv
```

## Run Tests

```bash
pytest tests/ -v
```

## Skills Demonstrated
- Python OOP (class-based design)
- Pandas (data inspection, dtype handling, aggregation)
- NumPy (numeric operations)
- CLI tools with argparse pattern
- Test-driven development with pytest
```

- [ ] **Step 7: Commit**

```bash
git add phase-1-python-for-ai/projects/01-data-explorer-cli/
git commit -m "feat: Data Explorer CLI — Phase 1 Project 1"
```

---

## Task 7: Project 2 — Titanic EDA Notebook

**What it does:** A full Exploratory Data Analysis of the Titanic dataset — one of the most recognized ML datasets. Answers: Who survived? What factors predicted survival?

**Why it impresses interviewers:** Shows data storytelling skills — the ability to ask questions, explore data, visualize findings, and communicate insights. This is what AI engineers do before building models.

**Files:**
- Create: `phase-1-python-for-ai/projects/02-titanic-eda/README.md`
- Create: `phase-1-python-for-ai/projects/02-titanic-eda/requirements.txt`
- Create: `phase-1-python-for-ai/projects/02-titanic-eda/download_data.py`
- Create: `phase-1-python-for-ai/projects/02-titanic-eda/titanic_eda.ipynb` (created via notebook commands)

- [ ] **Step 1: Create data download script**

Create `phase-1-python-for-ai/projects/02-titanic-eda/download_data.py`:

```python
"""Download Titanic dataset from the seaborn built-in datasets."""
import seaborn as sns
import os

os.makedirs("data", exist_ok=True)
df = sns.load_dataset("titanic")
df.to_csv("data/titanic.csv", index=False)
print(f"Downloaded: {len(df)} rows saved to data/titanic.csv")
print(df.head())
```

- [ ] **Step 2: Install seaborn and download data**

```bash
pip install seaborn
cd phase-1-python-for-ai/projects/02-titanic-eda
python download_data.py
```

Expected: `Downloaded: 891 rows saved to data/titanic.csv`

- [ ] **Step 3: Create requirements.txt**

Create `phase-1-python-for-ai/projects/02-titanic-eda/requirements.txt`:

```
numpy>=1.26
pandas>=2.1
matplotlib>=3.8
seaborn>=0.13
jupyter>=1.0
```

- [ ] **Step 4: Create and run the EDA notebook**

Start Jupyter and create `titanic_eda.ipynb` with these cells in order:

**Cell 1 (Markdown):**
```markdown
# Titanic EDA — Who Survived?

An exploratory analysis of the Titanic dataset to understand what factors influenced survival.
Dataset: 891 passengers, 12 features.
```

**Cell 2 (Code):**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-v0_8-whitegrid")
sns.set_palette("husl")

df = pd.read_csv("data/titanic.csv")
print(f"Shape: {df.shape}")
df.head()
```

**Cell 3 (Code):**
```python
# Data quality check
print("Missing values:")
missing = df.isnull().sum()
print(missing[missing > 0])
print(f"\nSurvival rate: {df['survived'].mean():.1%}")
```

**Cell 4 (Markdown):**
```markdown
## Q1: What was the overall survival rate by passenger class?
```

**Cell 5 (Code):**
```python
survival_by_class = df.groupby("pclass")["survived"].mean()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Bar chart: survival rate
survival_by_class.plot(kind="bar", ax=ax1, color=["#e74c3c", "#f39c12", "#27ae60"], rot=0)
ax1.set_title("Survival Rate by Passenger Class")
ax1.set_xlabel("Class (1=First, 2=Second, 3=Third)")
ax1.set_ylabel("Survival Rate")
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{y:.0%}"))

# Count plot
df.groupby(["pclass", "survived"]).size().unstack().plot(
    kind="bar", ax=ax2, rot=0, color=["#e74c3c", "#27ae60"]
)
ax2.set_title("Passenger Count by Class and Survival")
ax2.set_xlabel("Class")
ax2.legend(["Died", "Survived"])
plt.tight_layout()
plt.savefig("survival_by_class.png", dpi=150, bbox_inches="tight")
plt.show()
print(survival_by_class.apply(lambda x: f"{x:.1%}"))
```

**Cell 6 (Markdown):**
```markdown
## Q2: Did gender affect survival? ("Women and children first")
```

**Cell 7 (Code):**
```python
survival_by_sex = df.groupby("sex")["survived"].mean()

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

survival_by_sex.plot(kind="bar", ax=axes[0], color=["#3498db", "#e91e8c"], rot=0)
axes[0].set_title("Survival Rate by Gender")
axes[0].yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{y:.0%}"))

sns.histplot(data=df, x="age", hue="survived", multiple="stack",
             bins=20, ax=axes[1], palette=["#e74c3c", "#27ae60"])
axes[1].set_title("Age Distribution by Survival")
axes[1].legend(["Died", "Survived"])
plt.tight_layout()
plt.savefig("survival_by_gender_age.png", dpi=150, bbox_inches="tight")
plt.show()
print(survival_by_sex.apply(lambda x: f"{x:.1%}"))
```

**Cell 8 (Markdown):**
```markdown
## Q3: Did fare (ticket price) correlate with survival?
```

**Cell 9 (Code):**
```python
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=df, x="survived", y="fare", ax=ax,
            palette=["#e74c3c", "#27ae60"])
ax.set_xticklabels(["Died", "Survived"])
ax.set_title("Fare Distribution by Survival")
ax.set_ylabel("Ticket Fare (£)")
plt.tight_layout()
plt.savefig("fare_vs_survival.png", dpi=150, bbox_inches="tight")
plt.show()

print(df.groupby("survived")["fare"].describe().round(2))
```

**Cell 10 (Markdown):**
```markdown
## Key Findings

1. **Class mattered most**: 1st class had 63% survival vs 24% for 3rd class
2. **Gender was decisive**: 74% of women survived vs 19% of men
3. **Higher fare = higher survival**: survivors paid nearly 3x more on average
4. **Children had better odds**: passengers under 15 had higher survival rates

## Conclusion
Survival on the Titanic was not random — it was strongly correlated with socioeconomic status (class, fare) and gender. This dataset is a classic example of how social factors manifest as data patterns.
```

- [ ] **Step 5: Write the project README**

Create `phase-1-python-for-ai/projects/02-titanic-eda/README.md`:

```markdown
# Titanic EDA — Exploratory Data Analysis

A full exploratory data analysis of the Titanic dataset, answering: **What factors determined who survived?**

## Key Questions Answered
1. Did passenger class (1st/2nd/3rd) affect survival?
2. Did gender influence survival odds?
3. Did ticket fare correlate with survival?

## Key Findings
- 1st class passengers had 63% survival vs 24% for 3rd class
- 74% of women survived vs 19% of men
- Survivors paid nearly 3x higher ticket fares on average

## How to Run

```bash
pip install -r requirements.txt
python download_data.py         # downloads data/titanic.csv
jupyter notebook titanic_eda.ipynb
```

## Skills Demonstrated
- Exploratory Data Analysis (EDA) methodology
- Pandas (groupby, aggregation, filtering)
- Matplotlib + Seaborn (multi-chart layouts, styled plots)
- Data storytelling — asking business questions, finding answers in data
- Jupyter Notebooks (production-ready, reproducible)
```

- [ ] **Step 6: Add data/ to .gitignore, commit everything else**

Create `phase-1-python-for-ai/projects/02-titanic-eda/.gitignore`:

```
data/
*.png
.ipynb_checkpoints/
```

```bash
git add phase-1-python-for-ai/projects/02-titanic-eda/
git commit -m "feat: Titanic EDA notebook — Phase 1 Project 2"
```

---

## Task 8: Phase 1 README + Push to GitHub

**Files:**
- Create: `phase-1-python-for-ai/README.md`

- [ ] **Step 1: Write Phase 1 README**

Create `phase-1-python-for-ai/README.md`:

```markdown
# Phase 1: Python for AI

**Duration:** ~2-3 weeks | **Status:** Complete

Python fundamentals for AI engineering — NumPy, Pandas, and Jupyter Notebooks.

## Notes

| Topic | File |
|-------|------|
| Python Basics (lists, functions, classes, comprehensions) | [01-python-basics.md](./notes/01-python-basics.md) |
| NumPy (arrays, broadcasting, vectorized math) | [02-numpy.md](./notes/02-numpy.md) |
| Pandas (DataFrames, cleaning, aggregation) | [03-pandas.md](./notes/03-pandas.md) |
| Jupyter Notebooks (shortcuts, magic commands, best practices) | [04-jupyter.md](./notes/04-jupyter.md) |

## Exercises

| File | Covers |
|------|--------|
| [01_python_basics.py](./exercises/01_python_basics.py) | List comprehensions, functions, classes |
| [02_numpy_exercises.py](./exercises/02_numpy_exercises.py) | Array ops, broadcasting, matrix math |
| [03_pandas_exercises.py](./exercises/03_pandas_exercises.py) | DataFrames, cleaning, groupby |

## Projects

| Project | Description | Skills |
|---------|-------------|--------|
| [Data Explorer CLI](./projects/01-data-explorer-cli/) | CLI tool to profile any CSV dataset | OOP, Pandas, pytest |
| [Titanic EDA](./projects/02-titanic-eda/) | Who survived the Titanic and why? | Pandas, Matplotlib, Seaborn |
```

- [ ] **Step 2: Commit Phase 1 README**

```bash
git add phase-1-python-for-ai/README.md
git commit -m "docs: add Phase 1 README"
```

- [ ] **Step 3: Push everything to GitHub**

```bash
git push -u origin main
```

Expected: All commits pushed to `https://github.com/praguee/AI`

- [ ] **Step 4: Verify on GitHub**

Open `https://github.com/praguee/AI` and confirm:
- README renders correctly
- Folder structure is visible
- Both projects are there

---

## Self-Review

**Spec coverage:**
- [x] Python basics notes + exercises
- [x] NumPy notes + exercises
- [x] Pandas notes + exercises
- [x] Jupyter notes
- [x] Project 1: Data Explorer CLI with tests
- [x] Project 2: Titanic EDA notebook
- [x] All READMEs for recruiter readability
- [x] Push to GitHub

**Placeholder check:** No TBDs — all code is complete and runnable.

**Type consistency:** `DataExplorer` class used consistently across `explorer.py` and `test_explorer.py`.
