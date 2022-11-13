import numpy as np

n = 2000000
v = 290797
dim = 50515093
points = []

for _ in range(n):
    x = v
    v = (v ** 2) % dim
    y = v
    v = (v ** 2) % dim
    
    points.append((x, y))
    
m = 2000
length = dim//m + 1
grid = {(i, j): [] for i in range(m) for j in range(m)}

for point in points:
    a, b = point[0]//length, point[1]//length
    grid[a, b].append(point)
    
min_dist = 1e14

for i in range(m - 1):
    for j in range(m - 1):
        tmp_points = grid[i, j] + grid[i, j + 1] + grid[i + 1, j] + grid[i + 1, j + 1]
        
        for k in range(len(tmp_points) - 1):
            for l in range(k + 1, len(tmp_points)):
                d = ((tmp_points[k][0] - tmp_points[l][0]) ** 2 +
                     (tmp_points[k][1] - tmp_points[l][1]) ** 2)
                min_dist = min(min_dist, d)
                
min_dist = np.sqrt(min_dist)
print(round(min_dist, 9))
