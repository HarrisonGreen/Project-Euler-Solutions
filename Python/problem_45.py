import math

def number_search(limit):
    for i in range(286, limit + 1):
        t = i * (i + 1)/2
        if pentagon_check(1 + 24 * t) and hexagon_check(1 + 8 * t):
            print(int(t))

def pentagon_check(n):
    root = int(math.sqrt(n))
    if root * root == n and root % 6 == 5:
            return True
    return False

def hexagon_check(n):
    root = int(math.sqrt(n))
    if root * root == n and root % 4 == 3:
            return True
    return False

if __name__ == "__main__":
    number_search(100000)
