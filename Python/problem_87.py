import numpy as np
from time import time

lim = 50000000

# Get list of primes
primes = [2]
for i in range(3, int(np.sqrt(lim)), 2):
    for j in primes:
        
        if i%j == 0:
            break
        
        elif j > np.sqrt(i):
            primes.append(i)
            break
        
# Find expressible numbers
nums = set()

for prime_one in primes:
    p_one = prime_one**2
    rem_one = lim - p_one
    
    for prime_two in primes:
        p_two = prime_two**3
        if p_two > rem_one:
            break
        
        rem_two = rem_one - p_two
        
        for prime_three in primes:
            p_three = prime_three**4
            if p_three > rem_two:
                break
            
            nums.add(p_one + p_two + p_three)
            
print(len(nums))
