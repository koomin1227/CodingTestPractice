#https://www.acmicpc.net/problem/9461
from sys import stdin
from collections import deque
from itertools import product
import copy
import heapq
input=stdin.readline
t=int(input())
dp=[0,1,1,1,2,2]
for i in range(t):
    n=int(input())
    if n<len(dp):
        print(dp[n])
    else:
        length=len(dp)
        for j in range(length,n+1):
            tmp=dp[j-1]+dp[j-5]
            dp.append(tmp)
        print(dp[n])
    