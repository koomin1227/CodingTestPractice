#https://www.acmicpc.net/problem/12015
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


leng=1
for i in range(1,n):
    if se[leng]<series[i]:
        leng+=1
        se.append(series[i])
        continue
    tmp=binary(1,leng,series[i])
    se[tmp]=series[i]

print(leng)