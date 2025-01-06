import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
movement = {'U' : (-1, 0), 'R' : (0, 1), 'D' : (1, 0), 'L' : (0, -1)}
maze = []
for i in range(n):
    maze.append(input())

dp = [[0]*m for _ in range(n)]

def dfs(r, c):
    if r < 0 or r >= n or c < 0 or c >= m:
        return 1
    if dp[r][c] != 0:
        return dp[r][c]
    dp[r][c] = -1
    result = dfs(r + movement[maze[r][c]][0], c + movement[maze[r][c]][1])
    dp[r][c] = result
    return dp[r][c]

for r in range(n):
    for c in range(m):
        if dp[r][c] == 0:
            dfs(r, c)

answer = 0
for r in range(n):
    for c in range(m):
        if dp[r][c] == 1:
            answer += 1

print(answer)
