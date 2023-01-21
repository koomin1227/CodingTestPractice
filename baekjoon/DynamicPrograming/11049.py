#https://www.acmicpc.net/problem/11049
from sys import stdin
input=stdin.readline

n=int(input())
ma=[]
dp=[0]*n

for i in range(n):
    ma.append(list(map(int,input().split())))
dp[1]=ma[0][0]*ma[0][1]*ma[1][1]
for i in range(2,n):
    dp[i]=min(dp[i-1]+(ma[0][0]*ma[i][0]*ma[i][1]), dp[i-2]+(ma[i-1][0]*ma[i-1][1]*ma[i][1])+(ma[0][0]*ma[i-1][0]*ma[i][1]))
print(dp[n-1])