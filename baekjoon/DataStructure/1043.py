#https://www.acmicpc.net/problem/1043
from sys import stdin
from collections import deque
from itertools import product
import copy
import heapq
input=stdin.readline
n,m=map(int,input().split())
tmp=list(map(int,input().split()))
if tmp[0]==0:
    tn=0
    tlist=set()
else:
    tn=tmp[0]
    tlist=set(tmp[1:])
plist=[set() for _ in range(m)]
for i in range(m):
    plist[i]=list(map(int,input().split()))
    plist[i]=set(plist[i][1:])
while True:
    repu=True
    for i in range(m):
        if len(plist[i])!=0:
            tempset=tlist&plist[i]
            if len(tempset)!=0:
                repu=False
                tlist=tlist|plist[i]
                plist[i]=set()
    if repu==True:
        break
lie_num=0
for i in plist:
    if len(i)!=0:
        lie_num+=1
print(lie_num)    


