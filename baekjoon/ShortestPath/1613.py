# https://www.acmicpc.net/problem/1613

from sys import stdin
input = stdin.readline
INF=int(1e9)
n,m = map(int,input().split())

graph=[[INF]*(n+1)for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1

s = int(input())
query = []
for _ in range(s):
    query.append(list(map(int,input().split())))

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for a,b in query:
    if graph[a][b] >= 1 and graph[a][b] < INF:
        print(-1)
    elif graph[b][a] >= 1 and graph[b][a] < INF:
        print(1)
    else:
        print(0)
