from sys import stdin
input = stdin.readline
T = int(input())
answer = []
for t in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [[0] * (m + 1) for _ in range(n)]
    for i in range(1, m + 1):
        if i % coins[0] == 0:
            dp[0][i] = 1
    for i in range(1, n):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j] 
            for k in range(1, j//coins[i] + 1):
                if j - k*coins[i] == 0:
                    dp[i][j] += 1
                elif j - k*coins[i] > 0:
                    dp[i][j] += dp[i - 1][j - k*coins[i]]
    answer.append(dp[n-1][m])

for i in answer:
    print(i)