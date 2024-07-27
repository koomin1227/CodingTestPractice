n = int(input())
if n < 3:
    dp = [0] * (3)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 3
    print(dp[n])
else:
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2] * 2

    print(dp[n] % 10007)