import numpy as np

# Exercise 1: Basic array and math
prices = np.array([10, 20, 30, 40, 50])
print("Prices * 2:", prices * 2)
print("Prices + 100:", prices + 100)

# Exercise 2: Stats
scores = np.array([91, 87, 76, 94, 88])
print("Sum:", scores.sum())
print("Min:", scores.min())
print("Max:", scores.max())
print("Mean:", scores.mean())

# Exercise 3: Filtering
temperatures = np.array([36.6, 37.1, 38.5, 36.9, 39.2, 37.8])
fevers = temperatures[temperatures > 38]
print("Fever temperatures:", fevers)
print("Fever count:", len(fevers))

# Exercise 4: 2D array — rows and columns
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Shape:", data.shape)
print("First row:", data[0])
print("Second row:", data[1])
print("Value at row 1, col 2:", data[1][2])
print("First column:", data[:, 0])
print("Last column:", data[:, 2])
