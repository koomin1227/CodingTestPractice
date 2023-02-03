#https://www.acmicpc.net/problem/12851
from sys import stdin
from collections import deque
input=stdin.readline

n,k=map(int,input().split())
max_time=abs(n-k)+1
min_time=abs(n-k)+1
res=[0]*100001
tot=0
que=deque([[n,0]])
visited=[100000]*1000000
while que:
    now=que.popleft()
    
    if now[0]==k:
        res[now[1]]+=1
        min_time=min(min_time,now[1])
        continue
    if visited[now[0]]<now[1]:
        continue
    else:
        visited[now[0]]=now[1]
    if now[0]-1>=0:
        que.append([now[0]-1,now[1]+1])
    if now[0]+1-k<=100000:
        que.append([now[0]+1,now[1]+1])
    if now[0]*2-k<=100000:
        que.append([now[0]*2,now[1]+1])
print(min_time)
print(res[min_time])