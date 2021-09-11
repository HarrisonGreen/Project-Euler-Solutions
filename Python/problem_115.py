def main(m):
    A = {i:1 for i in range(m)}
    
    n = m - 1
    while True:
        n += 1
        A[n] = A[n-1] + sum(A[i] for i in range(n - m)) + 1
        if A[n] > 1000000:
            print(n)
            break
        
if __name__ == "__main__":
    main(50)
