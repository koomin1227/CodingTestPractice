from sys import stdin
from collections import deque
from itertools import combinations
import copy

n,m=map(int,stdin.readline().split())
virus=[]
lab=[]
space=[]
dy=[-1,0,1,0]
dx=[0,-1,0,1]
for i in range(n):
    tmp=list(map(int,stdin.readline().split()))
    lab.append(tmp)
    for j in range(m):
        if tmp[j]==2:
            virus.append([i,j])
        elif tmp[j]==0:
            space.append([i,j])

    
#위치 3개 뽑기
wall=list(combinations(space,3))


def bfs(y,x,n_lab):
    que=deque([])
    que.append([y,x])
    while que:
        now=que.popleft()
        for i in range(0,4):
            ny=now[0]+dy[i]
            nx=now[1]+dx[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if n_lab[ny][nx]>=1:
                continue
            if n_lab[ny][nx]==0:
                que.append([ny,nx])
                n_lab[ny][nx]=2
    return n_lab

def dfs(y,x):
    for i in range(0,4):
        ny=y+dy[i]
        nx=x+dx[i]
        if nx>=0 and nx<m and ny>=0 and ny<n:
            if n_lab[ny][nx]==0:
                n_lab[ny][nx]=2
                dfs(ny,nx)

maxi=0
for i in wall:
    tot=0
    
    n_lab=copy.deepcopy(lab)
    n_lab[i[0][0]][i[0][1]]=1
    n_lab[i[1][0]][i[1][1]]=1
    n_lab[i[2][0]][i[2][1]]=1
    #바이러스 퍼뜨리기
    for v in virus:
        dfs(v[0],v[1])
    #안전구역 세기
    for safe in n_lab:
        for safe2 in safe:
            if safe2==0:
                tot+=1
    if maxi<tot:
        maxi=tot

print(maxi)
    











    






