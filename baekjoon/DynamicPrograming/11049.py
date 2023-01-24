#https://www.acmicpc.net/problem/11049
from sys import stdin
input=stdin.readline

n=int(input())
ma=[]
dp=[[0]*n for _ in range(n)]

for i in range(n):
    ma.append(list(map(int,input().split())))
for i in range(1,n):
    for j in range(0,n-i):
        r,c=j,i+j
        dp[r][c]=2147483648
        for k in range(r,c):
            dp[r][c]=min(dp[r][c],dp[r][k]+dp[k+1][c]+(ma[r][0]*ma[k][1]*ma[c][1]))
for i in dp:
    print(i)

print(dp[0][n-1])

