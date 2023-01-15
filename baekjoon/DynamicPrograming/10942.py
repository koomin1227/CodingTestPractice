#https://www.acmicpc.net/problem/10942
from sys import stdin
input=stdin.readline

n=int(input())
ar=[-1]
ar=ar+list(map(int,input().split()))
m=int(input())
q=[]
dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    q.append(list(map(int,input().split())))
for i in range(1,n+1):
    dp[i][i]=True
for e in range(1,n+1):
    for s in range(1,e):
        dp[e][s]=(ar[e]==ar[s] and (e-1<s+1 or dp[e-1][s+1]==1))
for i in range(m):
    if dp[q[i][1]][q[i][0]]:
        print(1)
    else:
        print(0)
# for i in range(n):
#     print(dp[i])
