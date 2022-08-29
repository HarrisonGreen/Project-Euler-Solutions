import numpy as np
import math

n = 1000 # Number of coin flips
t = 9 # Log10 of £ target

def dh_by_df(f, n, t):
    return ((n/(1 - f)) * (np.log10(1 + 2 * f) - np.log10(1 - f)) +
            (n * np.log10(1 - f) - t) * (2/(1 + 2 * f) + 1/(1 - f)))

# Find optimal value of fraction, f
lower = 0.001
upper = 0.999

while upper - lower > 0.000001:
    mid = (upper + lower)/2
    if dh_by_df(mid, n, t) * dh_by_df(lower, n, t) > 0:
        lower = mid
    else:
        upper = mid

# Calculate min number of heads, h
f = (upper + lower)/2
h = math.ceil((t - n * np.log10(1 - f))/(np.log10(1 + 2 * f) - np.log10(1 - f)))

# Find probability of getting at least h heads
p = 0
for i in range(h, n + 1):
    p += math.comb(n, i)
    
p /= 2 ** n
print(round(p, 12))
