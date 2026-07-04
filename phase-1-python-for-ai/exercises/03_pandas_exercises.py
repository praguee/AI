import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("/home/parag/AI/phase-1-python-for-ai/exercises/employees.csv")

# Exercise 1: Basic exploration
print("Shape:", df.shape)
print("\nFirst 3 rows:")
print(df.head(3))

# Exercise 2: Select columns
print("\nSalaries:")
print(df["salary"])
print("\nNames and departments:")
print(df[["name", "department"]])

# Exercise 3: Filtering
print("\nSalary above 80000:")
print(df[df["salary"] > 80000])
print("\nDevOps employees:")
print(df[df["department"] == "DevOps"])
print("\nRating above 4.0:")
print(df[df["rating"] > 4.0])

# Exercise 4: Groupby
print("\nAverage salary per department:")
print(df.groupby("department")["salary"].mean())
print("\nHighest rating per department:")
print(df.groupby("department")["rating"].max())

# Exercise 5: Missing values
df.loc[2, "salary"] = np.nan
df.loc[5, "rating"] = np.nan
print("\nMissing values:")
print(df.isnull().sum())

# Fill missing salary with mean
df["salary"] = df["salary"].fillna(df["salary"].mean())
print("\nAfter filling missing salary:")
print(df.isnull().sum())

# Drop remaining missing rows
df = df.dropna()
print("\nAfter dropping missing rows:", df.shape)
