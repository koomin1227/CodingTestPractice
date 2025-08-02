# from sys import stdin
# input = stdin.readline
import sys
from collections import deque
sys.setrecursionlimit(100000)
dr = (1,0,-1,0)
dc = (0,-1,0,1)

n, m = map(int, input().split())
maze = []
for _ in range(m):
    maze.append(list(map(int, input())))
answer = 10000
que = deque()
que.append((0,0))

is_visited = [[-1] * n for _ in range(m)]
is_visited[0][0] = 0
cnt = 0
while que:
    r, c = que.popleft()
    cnt += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= m or nc < 0 or nc >= n:
            continue
        if is_visited[nr][nc] != -1:
            continue
        if maze[nr][nc] == 1:
            is_visited[nr][nc] = is_visited[r][c] + 1
            que.append((nr, nc))
        else:
            is_visited[nr][nc] = is_visited[r][c]
            que.appendleft((nr, nc))
print(is_visited[m - 1][n - 1])
