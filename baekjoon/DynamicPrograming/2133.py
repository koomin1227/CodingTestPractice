n = int(input())
dp = [0] * (n+1)
if n == 1:
    print(0)
else:
    dp[2] = 3
    for i in range(3, n + 1):
        if i % 2 == 1:
            continue
        else:
            dp[i] += dp[i - 2] * 3
            for j in range(2, i//2):
                dp[i] += dp[i - (j * 2)] * 2
            dp[i] += 2
    print(dp[n])