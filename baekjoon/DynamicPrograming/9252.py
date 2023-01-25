#https://www.acmicpc.net/problem/9252
from sys import stdin
from collections import deque
input=stdin.readline

str1=input()
str2=input()
len1=len(str1)-1
len2=len(str2)-1
dp=[[0]*(len2+1)for _ in range(len1+1)]
ans=deque([])
for i in range(1,len1+1):
    for j in range(1,len2+1):
        if str1[i-1]==str2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        dp[i][j]=max(dp[i][j],dp[i-1][j],dp[i][j-1])
i,j=len1,len2
while True:
    
    if dp[i-1][j]==dp[i][j]:
        i-=1
    elif dp[i-1][j]<dp[i][j]:
        j-=1
        ans.appendleft(str1[i-1])
        if dp[i-1][j]==0:
            break
print(dp[len1][len2])
for i in ans:
    print(i,end='')
#print(str(ans.reverse))

