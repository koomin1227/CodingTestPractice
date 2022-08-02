from sys import stdin
from collections import deque
from itertools import combinations
import copy
import heapq
input=stdin.readline
n=int(input())
dp=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    dp.append(tmp)
for k in range(0,n):
    for a in range(0,n):
        for b in range(0,n):
            if dp[a][k]+dp[k][b]==2:
                dp[a][b]=1
for i in range(n):
    for j in range(n):
        print(dp[i][j],end=' ')
    print()

