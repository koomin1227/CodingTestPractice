n = int(input())

dp = [0] * (n + 3)
dp[0] = 1
dp[1] = 1
dp[2] = 1
for i in range(3, n + 2):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n])