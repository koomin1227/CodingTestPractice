#https://www.acmicpc.net/problem/14003
from sys import stdin
input=stdin.readline

def binary(l,r,k):
    while(l<r):
        m=(l+r)//2
        if se[m]<k:
            l=m+1
        elif se[m]>=k:
            r=m
    else:
        return r
n=int(input())
series=list(map(int,input().split()))
se=[0,series[0]]
dp=[0]*n
dp[0]=1
leng=1
ans=[]
for i in range(1,n):
    if se[leng]<series[i]:
        leng+=1
        se.append(series[i])
        dp[i]=leng
        continue
    tmp=binary(1,leng,series[i])
    se[tmp]=series[i]
    dp[i]=tmp
current_leng=leng
for i in range(n-1,-1,-1):
    if dp[i]==current_leng:
        ans.append(series[i])
        current_leng-=1
print(leng)
print(*ans[::-1])