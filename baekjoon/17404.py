from sys import stdin
input = stdin.readline
INF = 100000000
n = int(input())
rgb = []
for i in range(n):
    tmp = list(map(int,input().split()))
    rgb.append(tmp)
ans = INF


for j in range(3):
    dp = [[INF]*3 for _ in range(n)]
    dp[0][j] = rgb[0][j]
    for i in range(1,n):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + rgb[i][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + rgb[i][2]
    for i in range(3):
        if j!=i:
            ans = min(ans,dp[-1][i])
print(ans)

