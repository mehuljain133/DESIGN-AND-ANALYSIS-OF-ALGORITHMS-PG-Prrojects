# Unit-VIII Dynamic Programming: Weighted Interval Scheduling, Segmented Least Square problem, Knapsack problem, Shortest Paths.

import bisect
import math

# ================================
# 1. Weighted Interval Scheduling
# ================================

def weighted_interval_scheduling(intervals):
    # intervals = [(start, end, weight)]
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    p = [0] * n

    # Compute p(j): rightmost non-conflicting interval before j
    for j in range(n):
        i = j - 1
        while i >= 0 and intervals[i][1] > intervals[j][0]:
            i -= 1
        p[j] = i

    M = [0] * (n + 1)
    for j in range(1, n + 1):
        M[j] = max(intervals[j - 1][2] + M[p[j - 1] + 1], M[j - 1])

    return M[n]

# ====================================
# 2. Segmented Least Squares Problem
# ====================================

def segmented_least_squares(points, C):
    """
    points: list of (x, y)
    C: penalty for each segment
    """
    points.sort()
    n = len(points)
    x = [0] + [pt[0] for pt in points]
    y = [0] + [pt[1] for pt in points]

    # Precompute error[i][j]
    error = [[0] * (n + 1) for _ in range(n + 1)]
    a = [[0] * (n + 1) for _ in range(n + 1)]
    b = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            m = j - i + 1
            sum_x = sum(x[i:j+1])
            sum_y = sum(y[i:j+1])
            sum_xy = sum(x[k]*y[k] for k in range(i, j+1))
            sum_x2 = sum(x[k]*x[k] for k in range(i, j+1))
            denom = m * sum_x2 - sum_x ** 2
            if denom == 0:
                a[i][j] = 0
                b[i][j] = sum_y / m
            else:
                a[i][j] = (m * sum_xy - sum_x * sum_y) / denom
                b[i][j] = (sum_y * sum_x2 - sum_x * sum_xy) / denom

            # compute squared error
            error[i][j] = sum(
                (y[k] - a[i][j]*x[k] - b[i][j])**2 for k in range(i, j+1)
            )

    # DP: OPT[j] = min_i (error[i][j] + OPT[i-1] + C)
    OPT = [0] * (n + 1)
    for j in range(1, n + 1):
        OPT[j] = min(error[i][j] + OPT[i - 1] + C for i in range(1, j + 1))

    return OPT[n]

# ==========================
# 3. 0/1 Knapsack Problem
# ==========================

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

# ===================================
# 4. Shortest Paths – Floyd-Warshall
# ===================================

def floyd_warshall(graph):
    """
    graph: 2D list, graph[i][j] = weight or inf
    """
    V = len(graph)
    dist = [row[:] for row in graph]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# ==========================
# Run All Examples
# ==========================

def test_all():
    print("=== Unit-VIII: Dynamic Programming ===\n")

    # 1. Weighted Interval Scheduling
    intervals = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (6, 7, 4), (5, 8, 11), (7, 9, 2)]
    result1 = weighted_interval_scheduling(intervals)
    print(f"Weighted Interval Scheduling Max Weight: {result1}")
    assert result1 == 17

    # 2. Segmented Least Squares
    points = [(1, 1), (2, 2), (3, 1.3), (4, 3.75), (5, 2.25), (6, 2.5)]
    penalty = 1
    result2 = segmented_least_squares(points, penalty)
    print(f"Segmented Least Squares Min Error: {result2:.2f}")

    # 3. Knapsack Problem
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    result3 = knapsack(weights, values, capacity)
    print(f"0/1 Knapsack Max Value: {result3}")
    assert result3 == 7

    # 4. Floyd-Warshall Shortest Paths
    inf = float('inf')
    graph = [
        [0,   3,   inf, 5],
        [2,   0,   inf, 4],
        [inf, 1,   0,   inf],
        [inf, inf, 2,   0]
    ]
    result4 = floyd_warshall(graph)
    print("Floyd-Warshall Shortest Paths:")
    for row in result4:
        print(row)

if __name__ == "__main__":
    test_all()
