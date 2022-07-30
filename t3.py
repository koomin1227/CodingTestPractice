from sys import stdin
from collections import deque
from itertools import combinations
import copy
import heapq
# input=stdin.readline
n=int(input())
mop=[]
for i in range(n):
    mop.append(list(input()))
dx=[-1,0,1,0]
dy=[0,-1,0,1]

def bfs(a,b):
    tot=0
    que=deque()
    que.append([a,b])
    mop[a][b]='2'
    tot+=1
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if mop[nx][ny]!='1':
                continue
            else:
                que.append([nx,ny])
                mop[nx][ny]='2'
                tot+=1
    return tot
apart=[]
apart_num=0
for i in range(n):
    for j in range(n):
        if mop[i][j]=='1':
            apart_num+=1
            apart.append(bfs(i,j))
apart.sort()
print(apart_num)
for i in apart:
    print(i)
