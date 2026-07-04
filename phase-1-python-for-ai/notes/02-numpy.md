# NumPy — Fast Math for AI

## Why NumPy?

Python lists don't do math the way you expect:

```python
prices = [10, 20, 30, 40, 50]
prices * 2    # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]  ❌ just copies the list
```

NumPy fixes this — it does real math on every number at once:

```python
import numpy as np

prices = np.array([10, 20, 30, 40, 50])
prices * 2    # [ 20  40  60  80 100]  ✅
```

NumPy is also 80x faster than Python loops because it runs in C under the hood.
In AI you do math on millions of numbers constantly — that's why NumPy exists.

---

## Creating an Array

```python
import numpy as np

scores = np.array([91, 87, 76, 94, 88])
```

---

## Basic Info

```python
print(scores)         # [91 87 76 94 88]
print(len(scores))    # 5  — you know this from lists
print(scores.shape)   # (5,) — NumPy way to get size
print(scores.dtype)   # int64 — what type of data is inside
```

`.shape` is important — it tells you the dimensions of your data:
- List of 5 numbers → `(5,)`
- Table of 100 rows, 3 columns → `(100, 3)`
- Image of 224x224 pixels, 3 colours → `(224, 224, 3)`

You will check `.shape` constantly in AI to make sure your data is the right size.

---

## Math Operations

```python
prices = np.array([10, 20, 30, 40, 50])

prices + 100    # [110 120 130 140 150]
prices - 5      # [  5  15  25  35  45]
prices * 2      # [ 20  40  60  80 100]
prices / 2      # [ 5. 10. 15. 20. 25.]
```

---

## Stats

```python
scores = np.array([91, 87, 76, 94, 88])

scores.sum()    # 436
scores.min()    # 76
scores.max()    # 94
scores.mean()   # 87.2
```

**In AI:** After training a model you get accuracy scores from 10 experiments. These four operations tell you the average, best, and worst instantly.

---

## Filtering — Finding Specific Values

```python
temperatures = np.array([36.6, 37.1, 38.5, 36.9, 39.2, 37.8])

temperatures > 38
# array([False, False,  True, False,  True, False])

temperatures[temperatures > 38]
# array([38.5, 39.2])

len(temperatures[temperatures > 38])
# 2  — count of fever patients
```

How it works:
- `temperatures > 38` → checks every number, returns True or False for each
- `temperatures[...]` → keeps only the True ones

**In AI:** "Give me only rows where confidence > 90%", "Give me only patients where age > 50" — this is filtering.

---

## 2D Arrays — Tables of Data

Real datasets are tables — rows and columns. NumPy handles this with 2D arrays:

```python
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(data.shape)    # (3, 3) — 3 rows, 3 columns
```

```
         col0  col1  col2
row 0  [  1     2     3  ]
row 1  [  4     5     6  ]
row 2  [  7     8     9  ]
```

---

## Grabbing Values from 2D Arrays

```python
data[0]         # first row  → [1, 2, 3]
data[1]         # second row → [4, 5, 6]
data[2]         # third row  → [7, 8, 9]

data[0][1]      # row 0, col 1 → 2
data[1][2]      # row 1, col 2 → 6
data[2][0]      # row 2, col 0 → 7

data[:, 0]      # all rows, col 0 → [1, 4, 7]  (first column)
data[:, 1]      # all rows, col 1 → [2, 5, 8]  (second column)
data[:, 2]      # all rows, col 2 → [3, 6, 9]  (third column)
```

The `:` in `data[:, 0]` means "all rows". Read it as: `[which rows, which column]`.

**In AI:** Your dataset has 1000 rows (patients) and 5 columns (age, weight, height...).
To grab just the age column: `dataset[:, 0]`

---

## Key Rules to Remember

| What you want | How to write it |
|---------------|-----------------|
| Whole array math | `array * 2` |
| Average | `array.mean()` |
| Filter values | `array[array > 60]` |
| Count filtered | `len(array[array > 60])` |
| One row | `data[0]` |
| One column | `data[:, 0]` |
| Specific value | `data[row][column]` |
