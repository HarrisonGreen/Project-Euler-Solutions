def count_tilings(n):
    A = {0:1, 1:1, 2:2, 3:4}
    
    for i in range(4, n + 1):
        A[i] = A[i - 1] + A[i - 2] + A[i - 3] + A[i - 4]
    
    return A[n]
        
if __name__ == "__main__":
    print(count_tilings(50))
    