import numpy as np

def find_continued_fraction_period(n):
    square_root = np.sqrt(n)
    target = (-int(square_root), 1)
    starting_point = target
    iterations = 0

    while True:
        iterations += 1

        denominator = (n - target[0] ** 2)//target[1]
        multiple = (square_root - target[0])//denominator
        target = (- target[0] - multiple * denominator, denominator)

        if target == starting_point:
            return iterations

def count_odd_periods(limit):
    count = 0

    for n in range(1, limit + 1):

        if int(np.sqrt(n)) ** 2 == n:
            continue
        
        if find_continued_fraction_period(n) % 2 == 1:
            count += 1

    print(count)

if __name__ == "__main__":
    count_odd_periods(10000)
