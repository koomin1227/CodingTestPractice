import sys
from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

input = sys.stdin.readline
n, m = map(int, input().split())

paper = []
for i in range(n):
    tmp = list(map(int,input().split()))
    paper.append(tmp)
def bfs():
    que = deque()
    que.append([0,0])
    paper[0][0] = -1
    while que:
        y, x = que.popleft()
        paper[y][x] = -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if (paper[ny][nx] > 0):
                    paper[ny][nx] += 1
                else:
                    if paper[ny][nx] == 0:
                        que.append([ny,nx])
                        paper[ny][nx] = -1
time = 0
while True:
    bfs()
    cheese = 0
    time += 1
    for i in range(n):
        for j in range(m):
            if paper[i][j] == -1 or paper[i][j] == 0:
                paper[i][j] = 0
            elif paper[i][j] >= 3:
                paper[i][j] = 0
            elif paper[i][j] < 3:
                paper[i][j] = 1   
                cheese += 1
    if cheese == 0:
        break
print(time)
