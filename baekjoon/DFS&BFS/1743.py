from collections import deque
dx = [1, 0 ,-1, 0]
dy = [0, 1, 0 ,-1]
n,m,k = map(int, input().split())
path = [[0] * m for _ in range(n)]
trashes = []
for _ in range(k):
    a,b = map(int, input().split())
    path[a - 1][b - 1] = 1
    trashes.append([a-1, b-1])
is_visit = [[0] * m for _ in range(n)]
ans = 0
for a, b in trashes:
    tot = 1
    que = deque()
    que.append([a,b])
    is_visit[a][b] = 1
    while que:
        now = que.popleft()
        for i in range(4):
            na = now[0] + dx[i]
            nb = now[1] + dy[i]
            if na < 0 or na >= n or nb < 0 or nb >= m:
                continue
            if path[na][nb] == 0 or is_visit[na][nb] == 1:
                continue
            que.append([na, nb])
            is_visit[na][nb] = 1
            tot += 1
    ans = max(ans, tot)
print(ans)