#https://www.acmicpc.net/problem/14938
from sys import stdin
input=stdin.readline
INF=int(1e9)
n,m,r=map(int,input().split())
t=[0]+list(map(int,input().split()))
dp=[[INF]*(n+1)for _ in range(n+1)]
for i in range(r):
    a,b,l=map(int,input().split())
    dp[a][b]=l
    dp[b][a]=l

for i in range(1,n+1):
    dp[i][i]=0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if dp[i][j]>dp[i][k]+dp[k][j]:
                dp[i][j]=dp[i][k]+dp[k][j]
maxi=0
for i in range(1,n+1):
    tot=0
    for j in range(1,n+1):
        if dp[i][j]<=m:
            tot+=t[j]
    maxi=max(maxi,tot)
print(maxi)