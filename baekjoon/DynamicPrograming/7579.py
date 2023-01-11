#https://www.acmicpc.net/problem/7579
from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
A=[0]+list(map(int,input().split()))
C=[0]+list(map(int,input().split()))
tot=sum(C)
res=tot+2
dp=[[0 for _ in range(tot+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,tot+1):
        if j<C[i-1]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],A[i-1]+dp[i-1][j-C[i-1]])
        if dp[i][j]>=m:
            res=min(res,j)
print(res)