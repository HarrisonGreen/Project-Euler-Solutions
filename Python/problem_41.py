from itertools import permutations
import numpy as np

def create_prime_list(limit):
    primes = [2]
    
    for i in range(3, limit, 2):
        square_root = np.sqrt(i)
        for prime in primes:
            if square_root < prime:
                primes.append(i)
                break
            if i % prime == 0:
                break
    
    return primes

def find_largest_prime(primes):
    digits = [1, 2, 3, 4, 5, 6, 7]
    largest = 0
    for order in permutations(digits):
        number = int("".join(map(str, order)))
        if is_prime(number, primes) and number > largest:
            largest = number
    print(largest)
        
def is_prime(number, primes):
    square_root = np.sqrt(number)
    for prime in primes:
        if prime > square_root:
            return True
        if number % prime == 0:
            return False
        
if __name__ == "__main__":
    limit = 3000
    primes = create_prime_list(limit)
    find_largest_prime(primes)
    