from collections import Counter

def count_solns(lim):
    count = {}

    for a in range(3, 5 * lim//4):
        for b in range(a//5 + 1, (a + 1)//2):

            n = (a - b) * (5 * b - a)

            if n >= lim:
                break

            count[n] = count.get(n, 0) + 1

    print(Counter(count.values())[10])

if __name__ == "__main__":
    count_solns(1000000)
