#https://www.acmicpc.net/problem/14719
from sys import stdin
from math import sqrt
from math import pow
from collections import deque

h,w = map(int,input().split())
bh = list(map(int,input().split()))
block = [[0] * w for _ in range(h)]
tot = 0
for i in range(w):
    for j in range(bh[i]):
        block[h - j - 1][i] = 1

for i in range(h):
    s=-1
    for j in range(w):
        if block[i][j] == 1 and s == -1:
            s = j
        elif block[i][j] == 1 and s!=-1:
            tot += (j-s)-1
            s=j
print(tot)   
