#https://www.acmicpc.net/problem/1707
from sys import stdin
from collections import deque
input=stdin.readline

k = int(input())
for _ in range(k):
    v,e=map(int,input().split())
    graph = [[] for _ in range(v + 1)]
    for i in range(e):
        s,e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    visited = [0] * (v + 1)
    que = deque()# number of node, 1 or -1 
    is_bipar=1
    for j in range(1,v+1):
        if visited[j] == 0:
            visited[j]=1
            que.append((j,1))
            while que:
                cur, ind = que.popleft()
                for i in graph[cur]:
                    if visited[i] == 0:
                        visited[i] = ind * -1
                        que.append((i, ind * -1))
                    elif visited[i] == ind:
                        is_bipar = 0
                        break
        if is_bipar==0:
            break

    if is_bipar:
        print('YES')
    else:
        print('NO')
