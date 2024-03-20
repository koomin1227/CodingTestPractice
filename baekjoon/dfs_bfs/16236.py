from sys import stdin
from collections import deque
input = stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(input())
space = []

for i in range(n):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        shark_position = [i, tmp.index(9)]
        tmp[tmp.index(9)] = 0
    space.append(tmp)
shark_size = 2
shark_capacity = 0
max_time = 0
def find_edible_fish(shark_size, shark_position):
    edible_fish = []
    is_visit = [[0] * (n) for _ in range(n)]
    que = deque()
    que.append(shark_position)
    is_visit[shark_position[0]][shark_position[1]] = 1
    min_time = 1000
    while que:
        y, x = que.popleft()
        if space[y][x] < shark_size and space[y][x] != 0:
            min_time = min(min_time, is_visit[y][x])
            edible_fish.append([y,x,is_visit[y][x] - 1])
            continue
        if min_time < is_visit[y][x]:
            continue
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if space[ny][nx] > shark_size:
                continue
            if is_visit[ny][nx] > 0:
                continue
            que.append([ny, nx])
            is_visit[ny][nx] = is_visit[y][x] + 1
    return sorted(edible_fish, key=lambda x:(x[2], x[0], x[1]))

while True:
    edible_fish = find_edible_fish(shark_size, shark_position)
    if len(edible_fish) == 0:
        break
    ny, nx, time = edible_fish[0]
    shark_position = [ny, nx]
    space[ny][nx] = 0
    max_time += time
    shark_capacity += 1
    if shark_capacity == shark_size:
        shark_size += 1
        shark_capacity = 0
print(max_time)

# for i in is_visit:
#     print(i)
# print(edible_fish)
# print(space)
