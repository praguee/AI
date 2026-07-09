# Jupyter Notebooks — The AI Engineer's Workbench

## Why Jupyter?

| Feature | .py file | Jupyter |
|---------|----------|---------|
| See output immediately | run whole file | one cell at a time |
| Charts embedded | popup window | right below code |
| Mix notes + code | only comments | Markdown cells |

AI engineers use Jupyter for exploration — write a line, see the result, adjust, run again. Much faster than `.py` files for data work.

---

## Starting Jupyter

```bash
jupyter notebook    # opens in browser at localhost:8888
```

Jupyter looks for files in the folder where the notebook is saved. Always use full paths when loading data:

```python
df = pd.read_csv("/home/parag/AI/phase-1-python-for-ai/exercises/employees.csv")
```

---

## Two Types of Cells

**Code cell** — runs Python, shows output below:
```python
df.describe()    # output appears right below
```

**Markdown cell** — formatted text, headings, notes. Change cell type from the dropdown at the top.

```markdown
## Who survived the Titanic?
This section explores survival rates by gender.
```

A real notebook looks like:
```
## Question          ← Markdown (your question)
code here            ← Code (your analysis)
output here          ← Output (the answer)
## Explanation       ← Markdown (your interpretation)
```

---

## Running Cells

| Shortcut | Action |
|----------|--------|
| `Shift + Enter` | Run cell, move to next |
| `Ctrl + Enter` | Run cell, stay on same cell |

---

## Adding and Deleting Cells

Press `Escape` first to enter command mode, then:

| Key | Action |
|-----|--------|
| `A` | Add cell above |
| `B` | Add cell below |
| `DD` | Delete cell |

---

## Displaying Data Without print()

In Jupyter, if the last line of a cell is a variable, it displays automatically — formatted as a table for DataFrames:

```python
df          # displays as a formatted table, no print() needed
df.shape    # displays (8, 5)
df.describe()  # displays full stats table
```

---

## Plotting

Charts appear embedded right below the cell — no popup windows:

```python
import matplotlib.pyplot as plt

# Bar chart
df["salary"].plot(kind="bar")
plt.title("Salaries")
plt.show()

# Count per category
df["department"].value_counts().plot(kind="bar")
plt.title("Employees per Department")
plt.show()
```

`value_counts()` counts how many times each value appears in a column. Used in AI to check class balance — if 99% of your data is one class, your model will be useless.

---

## describe() — First Thing to Run on Any Dataset

```python
df.describe()
```

Shows count, mean, min, max, and quartiles for every number column in one shot. Run this on every new dataset before doing anything else.
