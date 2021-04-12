dice = [4, 6, 8, 12, 20]
stats = {4: (5/2, 5/4)}

for i in range(1, 5):
    mean = stats[dice[i - 1]][0] * (dice[i] + 1)/2
    variance = stats[dice[i - 1]][0] * (dice[i] + 1)*(dice[i] - 1)/12 + stats[dice[i - 1]][1] * ((dice[i] + 1)/2) ** 2
    stats[dice[i]] = (mean, variance)

print(variance)
