from sys import stdin
from collections import deque
input = stdin.readline

dr = [1,0,-1,0]
dc = [0,-1,0,1]

n, m = map(int, input().split())
board = []

def bfs(is_visit, r,c):
    que = deque()
    que.append((r, c))
    is_visit[r][c] = 1

    while que:
        r, c = que.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if board[nr][nc] != 0 and is_visit[nr][nc] != 1:
                que.append((nr, nc))
                is_visit[nr][nc] = 1

def count_sea(r,c):
    count = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if board[nr][nc] == 0:
            count += 1
    return count

for _ in range(n):
    board.append(list(map(int, input().split())))
year = 0
while True:
    is_visit = [[0] * m for _ in range(n)]
    iceberg_count = 0
    for r in range(n):
        for c in range(m):
            if board[r][c] != 0 and is_visit[r][c] == 0:
                bfs(is_visit, r, c)
                iceberg_count += 1
    if iceberg_count > 1:
        break
    
    year += 1
    sea_counts = []

    for r in range(n):
        for c in range(m):
            if board[r][c] != 0:
                count = count_sea(r, c)
                if count > 0:
                    sea_counts.append((r,c,count))
    if len(sea_counts) == 0:
        break
    for r,c,count in sea_counts:
        board[r][c] = board[r][c] - count if board[r][c] - count >= 0 else 0

if iceberg_count > 1:
    print(year)
else:
    print(0)
    
    


    