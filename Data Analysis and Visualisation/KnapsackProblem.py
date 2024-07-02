def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# Values and weights of the items
values = [3, 4, 5, 6]
weights = [2, 3, 4, 5]
capacity = 5

# Solve knapsack problem
result = knapsack(values, weights, capacity)

# Display results
print('Maximum value:', result)
