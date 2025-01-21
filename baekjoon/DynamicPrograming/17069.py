from collections import deque
n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(3)]
dp[0][1][2] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if board[i - 1][j - 1] == 1:
            continue
        if dp[0][i][j] == 1:
            continue
        if board[i - 1][j - 2] != 1:
            dp[0][i][j] += dp[0][i][j - 1] + dp[2][i][j-1]
        if board[i - 2][j - 1] != 1:
            dp[1][i][j] += dp[1][i - 1][j] + dp[2][i - 1][j]
        if board[i - 2][j - 1] != 1 and board[i - 1][j - 2] != 1:
            dp[2][i][j] += dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

print(dp[0][n][n] + dp[1][n][n] + dp[2][n][n])
