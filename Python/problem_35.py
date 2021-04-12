import numpy as np

def create_primes_list(upper_limit):
    primes = [2]
    
    for i in range(3, upper_limit, 2):
        square_root = np.sqrt(i)
        for prime in primes:
            if square_root < prime:
                primes.append(i)
                break
            if i % prime == 0:
                break
    
    return primes

def remove_non_circular_primes(primes):
    bad_digits = ["0", "2", "4", "5", "6", "8"]
    to_remove = []
    for prime in primes:
        for digit in bad_digits:
            if digit in str(prime):
                to_remove.append(prime)
                break
    for prime in to_remove:
        primes.remove(prime)
    
    to_remove = []
    for prime in primes:
        for i in range(len(str(prime)) - 1):
            number = int(str(prime)[i+1:] + str(prime)[:i+1])
            if number not in primes:
                to_remove.append(prime)
                break
    for prime in to_remove:
        primes.remove(prime)
        
    print(len(primes) + 2)
    # 2 and 5 need to be included in the final count
    
if __name__ == "__main__":
    upper_limit = 1000000
    
    primes = create_primes_list(upper_limit)
    remove_non_circular_primes(primes)
    