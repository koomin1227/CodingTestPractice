#https://www.acmicpc.net/problem/12865
from sys import stdin
input=stdin.readline

n,k=map(int,input().split())
pro=[]
for i in range(n):
    a,b=map(int,input().split())
    pro.append([a,b])
dp=[[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        if pro[i-1][0]<=j:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-pro[i-1][0]]+pro[i-1][1])
        else:
            dp[i][j]=dp[i-1][j]

print(dp[n][k])
#잔디가 왜 안될까
