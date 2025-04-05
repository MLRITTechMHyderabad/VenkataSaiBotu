import numpy as np
points = np.array([
    [10, 25, 30, 22, 12, 18, 26, 32, 24, 29],
    [20, 15, 12, 28, 24, 26, 30, 18, 22, 25],
    [35, 30, 32, 40, 28, 34, 29, 31, 26, 37],
    [12, 18, 20, 15, 22, 14, 19, 21, 23, 17],
    [28, 26, 27, 25, 30, 29, 35, 32, 31, 38]
])

avgPoints = np.mean(points,axis=1)
print('Average points per game:')
print(avgPoints)

total = np.sum(points,axis=1)
max = np.argmax(total)
min = np.argmin(total)
print(f"Best-performing player: Player {max+1} (Total: {total[max]} points)")