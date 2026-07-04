# Python Basics

## Variables — Boxes with Labels

A variable is a box where you store something. You give it a name so you can use it later.

```python
name = "Parag"
age = 30
salary = 95000

print(name)       # Parag
print(age + 5)    # 35
```

---

## Lists — A Box That Holds Multiple Things

A list holds many values in order. Positions start at 0, not 1.

```python
skills = ["linux", "docker", "kubernetes"]

print(skills[0])    # linux   (first item)
print(skills[1])    # docker  (second item)
print(len(skills))  # 3

skills.append("ansible")
print(skills)       # ['linux', 'docker', 'kubernetes', 'ansible']
```

**In AI:** Your dataset is a list. A list of 10,000 rows. A list of model scores from 10 experiments.

---

## Dictionaries — A Box with Labels on Each Item

A dictionary stores values with a name (key) instead of a position number.

```python
employee = {
    "name": "Parag",
    "role": "DevOps Engineer",
    "experience": 5
}

print(employee["name"])         # Parag
print(employee["experience"])   # 5

employee["city"] = "Pune"       # add a new key
```

**In AI:** Every row in a dataset is a dictionary. Every model config is a dictionary.

---

## Loops — Do Something Many Times

Loop over a list — Python creates the loop variable automatically each time:

```python
skills = ["linux", "docker", "kubernetes"]

for skill in skills:
    print(skill)
# linux
# docker
# kubernetes
```

The name between `for` and `in` can be anything — Python creates it for you each loop. Pick a name that makes sense to read:

```python
for image in images:      # makes sense
for row in dataset:       # makes sense
for banana in skills:     # works, but confusing
```

Loop with a condition:

```python
scores = [0.91, 0.87, 0.94, 0.76, 0.88]

for score in scores:
    if score > 0.90:
        print(score, "- excellent!")
# 0.91 - excellent!
# 0.94 - excellent!
```

**In AI:** You train a model 100 times (100 epochs) — that's a loop. You process 10,000 images — that's a loop.

---

## Functions — Reusable Instructions

A function saves a block of code so you can run it anytime. Use `def` to define it.

```python
def greet(name):
    print("Hello", name)

greet("Parag")      # Hello Parag
greet("everyone")   # Hello everyone
```

Functions can give back a result using `return`:

```python
def add_tax(price):
    total = price * 1.18
    return total

result = add_tax(100)
print(result)    # 118.0
```

Real example — check if a score is passing:

```python
def is_passing(score):
    if score >= 60:
        return True
    return False

print(is_passing(75))    # True
print(is_passing(45))    # False
```

**In AI:** Everything is a function. Load data → function. Clean data → function. Train model → function. Predict → function.

---

## Putting It All Together

In AI you constantly combine all four concepts:

```python
scores = [0.91, 0.45, 0.87, 0.55, 0.94]

def is_passing(score):
    if score >= 0.60:
        return True
    return False

for score in scores:
    print(score, is_passing(score))

# 0.91 True
# 0.45 False
# 0.87 True
# 0.55 False
# 0.94 True
```

A loop, calling a function, on a list — that's how AI pipelines are written.

---

## Common Mistakes to Avoid

| Mistake | Wrong | Right |
|---------|-------|-------|
| Comparison operator | `=>` | `>=` |
| Typos in keywords | `Fale`, `true` | `False`, `True` |
| Colon at end of if/for/def | `if x > 5` | `if x > 5:` |
| Indentation | inconsistent spaces | always 4 spaces inside blocks |
