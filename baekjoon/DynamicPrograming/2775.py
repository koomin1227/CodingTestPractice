t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    dp = [[0]*(n + 1) for _ in range(k + 1)]
    for i in range(1, n + 1):
        dp[0][i] = dp[0][i - 1] + i
    for i in range(1, k + 1):
        for j in range(n + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    print(dp[k - 1][n])