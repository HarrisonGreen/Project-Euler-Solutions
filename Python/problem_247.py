from math import sqrt
from bisect import bisect

def find_min_size():
    gaps = [(1, 0, 0, 0)]
    sizes = [(sqrt(5) - 1)/2]
    min_size = 1

    while gaps:
        s = sizes[-1]
        x, y, l, b = gaps[-1]
        del gaps[-1]
        del sizes[-1]

        min_size = min(min_size, s)

        if l < 3:
            sizes.append((sqrt((x + s - y)**2 + 4) - x - y - s)/2)
            gaps.append((x + s, y, l + 1, b))

        if b < 3:
            sizes.append((sqrt((y + s - x)**2 + 4) - x - y - s)/2)
            gaps.append((x, y + s, l, b + 1))

    return min_size

def order_squares(min_size):
    gaps = [(1, 0, 0, 0)]
    sizes = [(sqrt(5) - 1)/2]
    n = 0
    count = 0

    while count < 20:
        n += 1
        s = sizes[-1]
        x, y, l, b = gaps[-1]
        del gaps[-1]
        del sizes[-1]

        size = (sqrt((x + s - y)**2 + 4) - x - y - s)/2
        if size >= min_size:
            pos = bisect(sizes, size)
            sizes.insert(pos, size)
            gaps.insert(pos, (x + s, y, l + 1, b))
        
        size = (sqrt((y + s - x)**2 + 4) - x - y - s)/2
        if size >= min_size:
            pos = bisect(sizes, size)
            sizes.insert(pos, size)
            gaps.insert(pos, (x, y + s, l, b + 1))

        if l == 3 and b == 3:
            count += 1
            if count == 20:
                print(n)

if __name__ == "__main__":
    min_size = find_min_size()
    order_squares(min_size)
