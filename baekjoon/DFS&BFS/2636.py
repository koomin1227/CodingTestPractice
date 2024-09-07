from collections import deque
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())

cheese = []

for i in range(n):
    cheese.append(list(map(int, input().split())))

tmp = 0
for i in range(n):
    for j in range(m):
        if cheese[i][j] == 1:
            tmp += 1
# if tmp == 0:
#     print(0)
#     print(0)
# else:
t = 0
r = tmp
while True:
    t += 1
    is_visited = [[0] * m for _ in range(n)]
    que = deque()
    que.append((0,0))
    is_visited[0][0] = 1
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if is_visited[ny][nx] == 1:
                continue
            if cheese[ny][nx] == 1:
                cheese[ny][nx] = 2
            elif cheese[ny][nx] == 0:
                que.append((ny, nx))
                is_visited[ny][nx] = 1
    remain_cheese = 0
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 2:
                cheese[i][j] = 0
            elif cheese[i][j] == 1:
                remain_cheese += 1
    if remain_cheese == 0:
        break
    r = remain_cheese
    

print(t)
print(r)
# for j in cheese:
#     print(j)


# print(cheese)
