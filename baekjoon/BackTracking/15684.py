from sys import stdin
input = stdin.readline

n, m, h = map(int,input().split())
ladder = [[0] * (n) for _ in range(h)]
answer = 4
for i in range(m):
    a,b = map(int, input().split())
    ladder[a - 1][b - 1] = 1
    ladder[a - 1][b] = -1

def check(ladder):
    for i in range(n):
        if i != down(ladder, i):
            return False
    return True

def down(ladder, i):
    x, y = i, 0
    while y < h:
        if ladder[y][x] != 0:
            x += ladder[y][x]
        y += 1
    return x

def dfs(depth, cur):
    global answer
    if depth > 3 or depth >= answer:
        return True
    if check(ladder):
        answer = min(answer, depth)
        return True
    for i in range(cur + 1, n * h):
        y, x = i // n, i % n
        if (ladder[y][x] != 0) or (x == n - 1) or (ladder[y][x + 1] != 0):
            continue
        ladder[y][x], ladder[y][x + 1] = 1, -1
        res = dfs(depth + 1, i)
        ladder[y][x], ladder[y][x + 1] = 0, 0
        if res:
            break

dfs(0, -1)
if answer == 4:
    print(-1)
else:
    print(answer)