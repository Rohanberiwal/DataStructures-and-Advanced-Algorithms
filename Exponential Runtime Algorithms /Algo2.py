import matplotlib.pyplot as plt
import time
import random

def maximum_cost(n, m, P):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    horizontal_costs = [[0] * m for _ in range(n)]
    vertical_costs = [[0] * (m + 1) for _ in range(n)]

    start_time = time.time()

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            horizontal_cuts = [P[k - 1][j - 1] + dp[i - k][j] for k in range(1, i + 1)]
            vertical_cuts = [P[i - 1][k - 1] + dp[i][j - k] for k in range(1, j + 1)]

            # Update dynamic programming table
            dp[i][j] = max(max(horizontal_cuts, default=0), max(vertical_cuts, default=0))

            # Store horizontal and vertical costs
            horizontal_costs[i - 1][j - 1] = max(horizontal_cuts, default=0)
            vertical_costs[i - 1][j] = max(vertical_cuts, default=0)

    end_time = time.time()
    return dp[n][m], end_time - start_time


input_sizes = [(10, 10), (20, 20), (30, 30), (40, 40)] 
runtimes = []

for n, m in input_sizes:
    prices = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]  
    max_cost, runtime = maximum_cost(n, m, prices)
    runtimes.append(runtime)
    print(f"Input size: ({n}, {m}), Runtime: {runtime:.6f} seconds")

sizes = [f"({n}, {m})" for n, m in input_sizes]
plt.plot(sizes, runtimes, marker='o')
plt.title('Runtime Analysis of maximum_cost Algorithm')
plt.xlabel('Input Size (n, m)')
plt.ylabel('Runtime (seconds)')
plt.grid(True)
plt.show()
