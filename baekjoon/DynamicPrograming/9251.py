#https://www.acmicpc.net/problem/9251
from sys import stdin
input=stdin.readline

str1=input()
str2=input()
len1=len(str1)-1
len2=len(str2)-1
dp=[[0]*(len2+1)for _ in range(len1+1)]
for i in range(1,len1+1):
    for j in range(1,len2+1):
        if str1[i-1]==str2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        dp[i][j]=max(dp[i][j],dp[i-1][j],dp[i][j-1])

print(dp[len1][len2])
