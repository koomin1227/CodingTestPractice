#https://www.acmicpc.net/problem/1520
from sys import stdin
import sys
sys.setrecursionlimit(100000)
input=stdin.readline
dx = [-1,0,1,0]
dy = [0,-1,0,1]
m,n = map(int,input().split())
graph = []
is_visit = [[-1]*n for _ in range(m)]
answer = 0
for i in range(m):
    tmp = list(map(int,input().split()))
    graph.append(tmp)

def dfs(x,y):
    if x == n-1 and y == m-1:
        return 1
    if is_visit[y][x] != -1:
        return is_visit[y][x]
    is_visit[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny >= 0 and ny < m:
            if graph[y][x]>graph[ny][nx]:
                is_visit[y][x]+=dfs(nx,ny)
    return is_visit[y][x]
answer = dfs(0,0)
for i in is_visit:
    print(i)
print(answer)



