from sys import stdin
from collections import deque
from itertools import product
import copy
import heapq
input=stdin.readline
v=int(input())
graph=[[]for _ in range(v+1)]
visited=[-1]*(v+1)
maxi=0
for i in range(v-1):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

que=deque()
que.append(1)
visited[1]=0
while que:
    n=que.popleft()
    for i in graph[n]:
        if visited[i[0]]==-1:
            que.append(i[0])
            visited[i[0]]=visited[n]+i[1]

que=deque()
que.append(visited.index(max(visited)))
max_tmp=visited.index(max(visited))
visited=[-1]*(v+1)
visited[max_tmp]=0
while que:
    n=que.popleft()
    for i in graph[n]:
        if visited[i[0]]==-1:
            que.append(i[0])
            visited[i[0]]=visited[n]+i[1]

print(max(visited))









