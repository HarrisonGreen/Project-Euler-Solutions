from numpy import sqrt
from math import floor

def is_square(x):
    root = floor(sqrt(x))
    return (root ** 2) == x

m = 0
solutions = []

while True:
    m += 1
    a = 5 * (m ** 2) - 1

    if is_square(a):
        n = 2 * m + floor(sqrt(a))
        l = int(sqrt(float(((2 * m * n) ** 2) + (((n ** 2) - (m ** 2)) ** 2))))
        solutions.append(l)

        if len(solutions) == 12:
            break
    
    a = 5 * (m ** 2) + 1

    if is_square(a):
        n = 2 * m + floor(sqrt(a))
        l = int(sqrt(float(((2 * m * n) ** 2) + (((n ** 2) - (m ** 2)) ** 2))))
        solutions.append(l)

        if len(solutions) == 12:
            break

print(sum(solutions))
