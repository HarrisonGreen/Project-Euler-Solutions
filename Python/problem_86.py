import math

def count_integer_solns(limit):
    count = 0

    a = 1
    while True:
        for s in range(2, 2 * a + 1):
                length = s * s + a * a

                if is_square(length):
                    count += min(s//2, (2 * a + 2 - s)//2)

                    if count >= limit:
                        return a

        a += 1

def is_square(x):
    return math.sqrt(x) % 1 == 0

if __name__ == "__main__":
    print(count_integer_solns(1000000))
