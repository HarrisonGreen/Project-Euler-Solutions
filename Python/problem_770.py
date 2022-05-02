lim = 1.9999
lim = lim/(4 - 2 * lim)
n = 1
x = 1

while True:
    n += 1
    x *= 2 * n/(2 * n - 1)

    if x > lim:
        print(n)
        break
