from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int,input().split()))
    dp = [[0]*k for i in range(k)]

    for i in range(1,k):
        dp[i-1][i] = files[i]+files[i-1]
    # print(dp)

    for i in range(2,k):
        for j in range(k-i):
            ni = i+j
            nj = j
            sum_r = sum(files[nj:ni+1])
            dp[nj][ni] = sum_r+dp[nj][nj]+dp[nj+1][ni]
            for m in range(nj,ni):
                dp[nj][ni] = min(dp[nj][ni],sum_r+dp[nj][m]+dp[m+1][ni])
    print(dp[0][k-1])
