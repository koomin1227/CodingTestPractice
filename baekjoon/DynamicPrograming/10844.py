n = int(input())

dp = [[0,1,1,1,1,1,1,1,1,1]]

for i in range(1, n):
    tmp = [0] * 10
    for j in range(10):
        if j == 0:
            tmp[j] = dp[i - 1][1]
        elif j == 9:
            tmp[j] = dp[i - 1][8]
        else:
            tmp[j] = dp[i - 1][j + 1] + dp[i - 1][j - 1]
    dp.append(tmp)

print(sum(dp[n - 1]) % 1000000000)
