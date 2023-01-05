#https://www.acmicpc.net/problem/2252
from collections import deque
from sys import stdin
input=stdin.readline
#입력
n,m=map(int,input().split())
graph=[[]for _ in range(n+1)]
inOrder=[0 for _ in range(n+1)]
que=deque()
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    inOrder[b]+=1
#위상정렬
for i in range(1,n+1):
    if inOrder[i]==0:
        que.append(i)
while que:
    x=que.popleft()
    print(x,end=' ')
    for i in graph[x]:
        inOrder[i]-=1
        if inOrder[i]==0:
            que.append(i)



