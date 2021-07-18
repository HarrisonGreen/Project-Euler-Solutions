from itertools import permutations

def find_maximix_arrangement(n, k):
    chars = [chr(i) for i in range(65, 65 + n)]
    maximum = 2 * n - 3
    count = 0
    
    for order in permutations(chars):
        order = "".join(order)

        if solve_order(order, n) == maximum:
            count += 1

            if count == k:
                return order


def solve_order(order, n):
    steps = 0
    for i in range(n):
        pos = order.index(chr(i + 65))

        if pos == i:
            pass

        elif pos == n - 1:
            order = order[:i] + order[i:][::-1]
            steps += 1

        else:
            order = order[:pos] + order[pos:][::-1]
            order = order[:i] + order[i:][::-1]
            steps += 2

    return steps

if __name__ == "__main__":
    print(find_maximix_arrangement(11, 2011))
