import numpy as np
import math

def generate_digits(b):
    n = len(str(b))
    k = 1
    digits = "2"

    while len(digits) <= n:

        l = math.ceil(np.log10(float(b)))
        
        x = (b // (10 ** (l - k))) * (10 ** (l - k))
        y = (b % (10 ** (l - k)))

        b = x * (y + (10 ** (l - k))) // (10 ** (l - k))
        a = str(b // (10 ** (l - k)))

        k = len(a)
        digits = digits + a

    return digits

guess = "2"
while len(guess) < 24:
    guess = generate_digits(int(guess))

print(f"{guess[0]}.{guess[1:]}")
