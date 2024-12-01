import numpy as np
import pandas as pd

df = pd.read_csv("day1_input.txt", sep="\s+", header=None)
data = df.values
a = np.sort(data[:, 0])
b = np.sort(data[:, 1])
print(f"Answer: {np.sum(np.abs(a - b))}")