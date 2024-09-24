n, t = map(int, input().split())

ks = [0]
ss = [0]
for i in range(n):
    k, s = map(int, input().split())
    ks.append(k)
    ss.append(s)

dp = [[0] * (t + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(t + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif j >= ks[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i-1][j - ks[i]] + ss[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][t])