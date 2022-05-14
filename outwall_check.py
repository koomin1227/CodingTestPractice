from collections import deque
from sys import stdin
from itertools import combinations
import copy
n,k=map(int,stdin.readline().split())
test=[]
virus=[]
n_virus=[[]]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
for i in range(n):
    tmp=list(map(int,stdin.readline().split()))
    test.append(tmp)
    for j in range(n):
        if tmp[j]!=0:
            virus.append([tmp[j],0,i,j])
virus.sort()
que=deque(virus)
s,x,y=map(int,stdin.readline().split())
while que:
    v,ts,tx,ty=que.popleft()
    if ts==s:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if test[nx][ny]==0:
                test[nx][ny]=v
                que.append([v,ts+1,nx,ny])


print(test[x-1][y-1])

