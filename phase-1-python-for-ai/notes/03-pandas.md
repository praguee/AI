# Pandas — Working with Real Data Tables

## What is Pandas?

NumPy handles arrays of numbers. But real data looks like this:

```
name      age    salary    department
Parag     30     95000     DevOps
Alice     25     70000     Engineering
Bob       32     88000     HR
```

A table with rows, columns, and mixed data types (text + numbers). This is called a **DataFrame** in Pandas.

---

## Loading Data

```python
import pandas as pd

# Create a DataFrame manually
data = {
    "name": ["Parag", "Alice", "Bob"],
    "age": [30, 25, 32],
    "salary": [95000, 70000, 88000]
}
df = pd.DataFrame(data)

# Load from a CSV file (most common in real life)
df = pd.read_csv("employees.csv")
```

---

## First Look at Your Data

```python
df.head()       # first 5 rows (preview)
df.head(10)     # first 10 rows
df.shape        # (rows, columns) — e.g. (8, 5)
df.info()       # column names, data types, missing value count
```

**What info() tells you:**
- Column names
- Data type of each column (int64, float64, str)
- Non-Null Count — how many rows have a value (missing = not counted)
- Memory usage — how much RAM this table uses

---

## Selecting Columns

```python
df["salary"]                  # one column
df[["name", "salary"]]        # two columns — pass a list
```

Double brackets because you're passing a list of column names inside `df[...]`.

---

## Filtering Rows

Works exactly like NumPy — inner condition gives True/False, outer keeps True rows:

```python
df[df["salary"] > 80000]          # employees earning above 80k
df[df["department"] == "DevOps"]  # DevOps employees only
df[df["rating"] > 4.0]            # high rated employees
```

Always use numbers without quotes when comparing number columns:
```python
df[df["rating"] > "4.0"]   # ❌ TypeError — "4.0" is text
df[df["rating"] > 4.0]     # ✅ correct
```

---

## Groupby — Summary by Category

Split the table into groups and calculate stats for each group:

```python
df.groupby("department")["salary"].mean()    # avg salary per dept
df.groupby("department")["salary"].max()     # highest salary per dept
df.groupby("department")["experience"].mean() # avg experience per dept
df.groupby("department")["rating"].min()     # lowest rating per dept
```

Read it as three steps:
```
df.groupby("department")  →  split table into groups (one per department)
["salary"]                →  look at the salary column in each group
.mean()                   →  calculate the average for each group
```

---

## Missing Values

Real datasets always have missing values. `NaN` means "Not a Number" — a missing value.

```python
import numpy as np

df.isnull().sum()    # count missing values per column
# name          0
# salary        1   ← one missing value here
# rating        1   ← one missing value here
```

**Fix missing values — two options:**

```python
# Option 1: Fill with average (keeps all rows)
df["salary"] = df["salary"].fillna(df["salary"].mean())

# Option 2: Drop rows with any missing value
df = df.dropna()
```

**Important:** `fillna()` and `dropna()` don't change the original table.
You must reassign to save the change:
```python
df["salary"] = df["salary"].fillna(...)   # ✅ saved
df["salary"].fillna(...)                  # ❌ not saved, original unchanged
```

---

## df.loc vs df.iloc

Two ways to point to a specific cell:

```python
df.loc[2, "salary"]    # row 2, column named "salary"  — use labels
df.iloc[2, 2]          # row 2, column position 2       — use positions
```

`.loc` is more readable, most people use it.

---

## Key Rules to Remember

| What | How |
|------|-----|
| Load CSV | `pd.read_csv("file.csv")` |
| Preview | `df.head()` |
| Size | `df.shape` |
| Column types + missing | `df.info()` |
| One column | `df["salary"]` |
| Two columns | `df[["name", "salary"]]` |
| Filter rows | `df[df["salary"] > 80000]` |
| Group summary | `df.groupby("dept")["salary"].mean()` |
| Find missing | `df.isnull().sum()` |
| Fill missing | `df["col"] = df["col"].fillna(df["col"].mean())` |
| Drop missing rows | `df = df.dropna()` |
