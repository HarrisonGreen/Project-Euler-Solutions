def count_tilings(n, m):
    A = {i: 1 for i in range(m)}
    
    for i in range(m, n + 1):
        A[i] = A[i - 1] + A[i - m]
        
    return A[n] - 1
        
if __name__ == "__main__":
    print(sum(count_tilings(50, m) for m in [2, 3, 4]))
    