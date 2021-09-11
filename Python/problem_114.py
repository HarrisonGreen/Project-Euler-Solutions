A = {0:1, 1:1, 2:1}

for n in range(3, 51):
    A[n] = A[n-1] + sum(A[i] for i in range(n - 3)) + 1

print(A[50])
