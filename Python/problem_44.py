import math

def pentagon_search(limit):
    for i in range(2, limit + 1):
        for j in range(1, i):
            P_i = i * (3 * i - 1)/2
            P_j = j * (3 * j - 1)/2
            S = P_i + P_j
            D = P_i - P_j
            if pentagon_check(1 + 24 * S) and pentagon_check(1 + 24 * D):
                    print(int(D))

def pentagon_check(n):
    root = int(math.sqrt(n))
    if root * root == n and root % 6== 5:
        return True
    return False

if __name__ == "__main__":
    pentagon_search(2500)
