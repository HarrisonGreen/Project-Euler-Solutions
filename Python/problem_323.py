import numpy as np
import math

def calculate_expectation(length):
    expect = np.zeros(length + 1)
    expect[1] = 2

    for n in range(2, length + 1):
        expect[n] = (sum(choose(n, k) * expect[k] for k in range(1, n)) + 2 ** n)/((2 ** n) - 1)
    
    print(expect[length])
    
def choose(n, k):
    return math.factorial(n)/(math.factorial(k) * math.factorial(n - k))

if __name__ == "__main__":
    calculate_expectation(32)
