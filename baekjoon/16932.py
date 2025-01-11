import sys
from collections import deque

input = sys.stdin.readline

dr = [1,0,-1,0]
dc = [0,1,0,-1]


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
size = 0

def bfs(s_r, s_c, is_visited, idx):
    size = 0
    que = deque()
    que.append((s_r,s_c))
    is_visited[s_r][s_c] = idx
    while que:
        r, c = que.popleft()
        size += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue  
            if board[nr][nc] == 0 or is_visited[nr][nc] != 0:
                continue  
            is_visited[nr][nc] = idx
            que.append((nr, nc))
    return size


shape_dict = {}
is_visited = [[0] * m for _ in range(n)]
idx = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and is_visited[i][j] == 0:
            size = bfs(i,j,is_visited, idx)
            shape_dict[idx] = size
            idx += 1
            
max_size = 0
for i in range(n):
    for j in range(m):
        if is_visited[i][j] == 0:
            size = 1
            id_set = set()
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                if is_visited[nr][nc] != 0 and is_visited[nr][nc] not in id_set:
                    id_set.add(is_visited[nr][nc])
                    size += shape_dict[is_visited[nr][nc]]
            max_size = max(max_size, size)
print(max_size)
