import numpy as np

def count_grid_traversals(n, d):
    grid = np.zeros([n, d])
    grid[:, 0] = 1
    grid[0, :] = 1
    
    for i in range(1, n):
        for j in range(1, d):
            grid[i, j] = grid[i, j - 1] + grid[i - 1, j]

    return grid[-2, -1] + grid[-1, -1] - 10 * (d - 1) - 2


if __name__ == "__main__":
    n = 11
    d = 101
    print(int(count_grid_traversals(n, d)))
