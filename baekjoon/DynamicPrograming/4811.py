while True:
    n = int(input())
    if n == 0:
        break
    dp = [[0] * (n + 1) for _ in range(n+1)]
    for i in range(1, n + 1):
        dp[0][i] = 1
    for h in range(1, n + 1):
        for w in range(1, n + 1):
            if h > w:
                continue
            dp[h][w] = dp[h - 1][w]
            if dp[h][w - 1] != 0:
                dp[h][w] += dp[h][w - 1]
    print(dp[n][n])