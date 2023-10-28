from sys import stdin
from collections import deque
input = stdin.readline

k = int(input())
w,h = map(int,input().split())
world = []
for i in range(h):
    world.append(list(map(int, input().split())))
que = deque()
que.append([0,0,0])
dx = [-1,0,1,0]
dy = [0,1,0,-1]
hx = [2, 1, -1, -2, -2, -1, 1, 2]
hy = [1, 2, 2, 1, -1, -2, -2, -1]
isVisit = [[[0]*(k+1) for _ in range(w)] for _ in range(h)] 

isVisit[0][0][0] = 1
while(que):
    cur_x, cur_y, cur_z = que.popleft()
    for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]
        if next_x<0 or next_x >= w or next_y < 0 or next_y >= h:
            continue
        if world[next_y][next_x] == 1:
            continue
        if isVisit[next_y][next_x][cur_z] == 0:
            isVisit[next_y][next_x][cur_z] = isVisit[cur_y][cur_x][cur_z] + 1
            que.append([next_x,next_y, cur_z]) 
    for i in range(8):
        next_x = cur_x + hx[i]
        next_y = cur_y + hy[i]
        if next_x<0 or next_x >= w or next_y < 0 or next_y >= h:
            continue
        if world[next_y][next_x] == 1:
            continue
        if cur_z < k:
            if isVisit[next_y][next_x][cur_z + 1] == 0:
                isVisit[next_y][next_x][cur_z + 1] = isVisit[cur_y][cur_x][cur_z] + 1
                que.append([next_x,next_y, cur_z + 1])
res = isVisit[h-1][w-1]
ans = []
for i in res:
    if i != 0:
        ans.append(i)
if len(ans) == 0:
    print(-1)
else: 
    print(min(ans) - 1)


