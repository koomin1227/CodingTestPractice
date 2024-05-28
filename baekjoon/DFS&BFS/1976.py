# https://www.acmicpc.net/problem/1976
from sys import stdin
input = stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1:
            graph[i].append(j+1)
        # graph[j + 1].append(i)
plan = list(map(int, input().split()))
isVisited = [0] * (n+1)

def dfs(cur):
    for i in graph[cur]:
        if isVisited[i] == 0:
            isVisited[i] = 1
            dfs(i)
isVisited[plan[0]] = 1
dfs(plan[0])

available = 1
for i in plan:
    if isVisited[i] == 0:
        available = 0
        break
if available == 1:
    print("YES")
else:
    print("NO")