import numpy as np

primes = [2]

for i in range(3, 1000000, 2):
    root = np.sqrt(i)

    for j in primes:

        if j > root:
            primes.append(i)
            break

        if i % j == 0:
            break

total = 0

for i in primes[1:]:
    total += 2/(i+1) + 7/18 * (i-3)/(i+1)

total /= (len(primes) - 1)
print(round(total, 10))
