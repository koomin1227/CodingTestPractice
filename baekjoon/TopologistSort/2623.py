#https://www.acmicpc.net/problem/2623
from sys import stdin
from collections import deque
input=stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
indegree=[0 for _ in range(n+1)]
que=deque([])
ans=[]
for i in range(m):
    tmp=list(map(int,input().split()))
    for i in range(1,tmp[0]):
        graph[tmp[i]].append(tmp[i+1])
        indegree[tmp[i+1]]+=1
for i in range(1,n+1):
    if indegree[i]==0:
        que.append(i)
while(que):
    node=que.popleft()
    ans.append(node)
    for i in graph[node]:
        indegree[i]-=1
        if indegree[i]==0:
            que.append(i)
if len(ans)==n:
    for i in ans:
        print(i) 
else:
    print(0)

