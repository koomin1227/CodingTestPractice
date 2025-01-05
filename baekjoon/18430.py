n, m = map(int, input().split())

kinds = [((0, -1),(1, 0)), ((0, -1),(-1, 0)), ((0, 1),(-1, 0)), ((0, 1),(1, 0))]

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
max_strength = 0

def is_out(r, c):
    global n, m
    return r < 0 or r >= n or c < 0 or c >= m
        

def dfs(now,is_visit, strength):
    global max_strength

    max_strength = max(max_strength, strength)
    for idx in range(now[0] * m + now[1] + 1, n * m):
        i = idx // m
        j = idx % m
        if is_visit[i][j] == 1:
            continue
        for kind in kinds:
            left = (i + kind[0][0], j + kind[0][1])
            right = (i + kind[1][0], j + kind[1][1])

            if is_out(left[0], left[1]) or is_out(right[0], right[1]):
                continue
            if is_visit[left[0]][left[1]] == 1 or is_visit[right[0]][right[1]] == 1:
                continue

            new_strength = board[i][j] * 2 + board[left[0]][left[1]] + board[right[0]][right[1]]
            is_visit[i][j] = 1
            is_visit[left[0]][left[1]] = 1
            is_visit[right[0]][right[1]] = 1

            dfs((i, j), is_visit, strength + new_strength)

            is_visit[i][j] = 0
            is_visit[left[0]][left[1]] = 0
            is_visit[right[0]][right[1]] = 0

is_visit = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        dfs((i,j), is_visit, 0)
print(max_strength)