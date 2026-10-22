E = {1:0}

for i in range(2, 31):
    E[i] = E[i-1] + (2**(i-1) - 1)/i

print(round(E[30], ndigits=2))
