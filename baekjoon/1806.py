#https://www.acmicpc.net/problem/1806
from sys import stdin
input=stdin.readline

n,s=map(int,input().split())
pro=list(map(int,input().split()))
l=n-1
f=0
r=0
min_len=n
tot=pro[0]
while r<n:
    if f<n-1:
        if tot>=s:
            min_len=min(min_len,f-r+1)
            if f==r:
                f+=1
                tot+=pro[f]
            else:
                tot-=pro[r]
                r+=1
        elif tot<s:
            f+=1
            tot+=pro[f]  
    else:
        if tot>=s:
            min_len=min(min_len,f-r+1)
        tot-=pro[r]
        r+=1
print(min_len)

