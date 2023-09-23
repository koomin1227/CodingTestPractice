# https://www.acmicpc.net/problem/1516
from sys import stdin
from collections import deque
input=stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
graph_in = [[] for _ in range(n + 1)]
indegree = [0] * (n+1)
times = [0] * (n+1)

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    times[i] = tmp[0]
    for j in tmp[1:-1]:
        # if j != -1:
        graph[j].append(i)
        graph_in[i].append(j)
        indegree[i] += 1
que = deque()
sequence = [-1]

for i in range(1,n+1):
    if indegree[i] == 0:
        que.append(i)

while que:
    now = que.popleft()
    sequence.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            que.append(i)

result = [0] * (n+1)
for i in range(1,n+1):
    now = sequence[i]
    if len(graph_in[now]) == 0:
        result[now] = times[now]
    else:
        prev = [0,0]
        for j in graph_in[now]:
            if result[j] >= prev[1]:
                prev = [j, result[j]]
        result[now] = times[now] + result[prev[0]]

for i in result[1:]:
    print(i)
