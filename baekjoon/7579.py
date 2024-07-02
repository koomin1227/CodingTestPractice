n, m  = map(int, input().split())

bytes = list(map(int, input().split()))
costs = list(map(int, input().split()))

total_cost = sum(costs)
result = total_cost + 1

dp = [[0] * (total_cost + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    byte = bytes[i - 1]
    cost = costs[i - 1]
    for j in range(0, total_cost + 1):
        if cost > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + byte)
        if m <= dp[i][j]:
            result = min(result, j)

print(result)