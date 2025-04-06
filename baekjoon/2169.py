from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
mars = []
for _ in range(n):
    mars.append(list(map(int, input().split())))
dp = [[0] * m for _ in range(n)]
tot = 0
for i in range(m):
    dp[0][i] = tot + mars[0][i]
    tot += mars[0][i]

for i in range(1, n):
    left_dp = [0] * m
    right_dp = [0] * m
    for j in range(m):
        if j == 0:
            right_dp[j] = dp[i - 1][j] + mars[i][j]
        else:
            right_dp[j] = max(dp[i - 1][j] + mars[i][j], right_dp[j - 1] + mars[i][j])
    for j in range(m - 1, -1, -1):
        if j == m - 1:
            left_dp[j] = dp[i - 1][j] + mars[i][j]
        else:
            left_dp[j] = max(dp[i - 1][j] + mars[i][j], left_dp[j + 1] + mars[i][j])
    for j in range(m):
        dp[i][j] = max(left_dp[j], right_dp[j])



print(dp[n - 1][m - 1])