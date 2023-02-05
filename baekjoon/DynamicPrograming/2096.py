#https://www.acmicpc.net/problem/2096
from sys import stdin
input=stdin.readline
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
dp=[[0,0,0],[0,0,0]]
dp_min=[[0,0,0],[0,0,0]]
dp[0][0],dp[0][1],dp[0][2]=arr[0][0],arr[0][1],arr[0][2]
dp_min[0][0],dp_min[0][1],dp_min[0][2]=arr[0][0],arr[0][1],arr[0][2]
for i in range(1,n):
    dp[1][0]=max(arr[i][0]+dp[0][0],arr[i][0]+dp[0][1])
    dp[1][1]=max(arr[i][1]+dp[0][0],arr[i][1]+dp[0][1],arr[i][1]+dp[0][2])
    dp[1][2]=max(arr[i][2]+dp[0][1],arr[i][2]+dp[0][2])
    dp[0][0],dp[0][1],dp[0][2]=dp[1][0],dp[1][1],dp[1][2]

    dp_min[1][0]=min(arr[i][0]+dp_min[0][0],arr[i][0]+dp_min[0][1])
    dp_min[1][1]=min(arr[i][1]+dp_min[0][0],arr[i][1]+dp_min[0][1],arr[i][1]+dp_min[0][2])
    dp_min[1][2]=min(arr[i][2]+dp_min[0][1],arr[i][2]+dp_min[0][2])
    dp_min[0][0],dp_min[0][1],dp_min[0][2]=dp_min[1][0],dp_min[1][1],dp_min[1][2]
print(max(dp[0][0],dp[0][1],dp[0][2]),end=' ')
print(min(dp_min[0][0],dp_min[0][1],dp_min[0][2]))