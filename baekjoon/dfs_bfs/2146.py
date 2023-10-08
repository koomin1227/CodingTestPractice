# https://www.acmicpc.net/problem/2146

from sys import stdin
from collections import deque
input = stdin.readline
n = int(input())
world = []
for i in range(n):
    world.append(list(map(int,input().split())))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
island_cnt = 1
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if world[i][j] == 1:
            island_cnt += 1
            que = deque()
            que.append([i,j])
            visited[i][j] = 1
            while que:
                cur_y, cur_x = que.popleft()
                world[cur_y][cur_x] = island_cnt
                for k in range(4):
                    ny = cur_y + dy[k]
                    nx = cur_x + dx[k]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n and world[ny][nx] == 1 and visited[ny][nx] == 0:
                        que.append([ny,nx])
                        visited[ny][nx] = 1
ans = 10000
que = deque()
def bfs(island_num):
    global ans
    for i in range(n):
        for j in range(n):
            if world[i][j] == island_num:
                que.append([i,j])
    while(que):
        cur_y, cur_x = que.popleft()
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if world[ny][nx] == 0:
                    if world[cur_y][cur_x] == island_num:
                        world[ny][nx] = -1
                    else:
                        world[ny][nx] = world[cur_y][cur_x] - 1
                    que.append([ny,nx])
                elif world[ny][nx] > 1 and world[ny][nx] != island_num:
                    ans = min(ans, world[cur_y][cur_x] * -1)
for island_num in range(2, island_cnt + 1):
    for i in range(n):
        for j in range(n):
            if world[i][j] < 0:
                world[i][j] = 0
    bfs(island_num)
                 
print(ans)

