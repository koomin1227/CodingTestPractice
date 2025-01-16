n = int(input())
k = int(input())

dp = [[0] * (k + 1) for _ in range(n + 1)]
# dp[1][1] = 1
for i in range(0, n + 1):
    for j in range(0, k + 1):
        if j == 1:
            dp[i][j] = i
        elif j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % 1000000003
answer = dp[n-3][k-1] + dp[n-1][k]
print(answer % 1000000003)
