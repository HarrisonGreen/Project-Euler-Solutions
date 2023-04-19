import numpy as np

n = 10000000
m = np.arange(2, n + 1)

p = (m - 1) * (n // (m - 1))
t = (p - m + 1) * p / (2 * (m - 1)) + (n - p) * (n // (m - 1))

print(int(sum(t)))
