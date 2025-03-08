import numpy as np
from scipy import stats

# Sample Data
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Mean, Median, Mode
print("Mean:", np.mean(data))
print("Median:", np.median(data))

# Fix for mode extraction
mode_result = stats.mode(data, keepdims=True)  # Ensure correct format
print("Mode:", mode_result.mode[0])
