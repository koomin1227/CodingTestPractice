#https://www.acmicpc.net/problem/9375
from sys import stdin
from collections import deque
from itertools import product
import copy
import heapq
input=stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    dic={}
    for i in range(n):
        Name,Sort=map(str,input().rstrip().split())
        if Sort in dic:
            dic[Sort]+=1
        else:
            dic[Sort]=1
    cnt=1
    for k in dic:
        cnt=cnt*(dic[k]+1)
    print(cnt-1)
