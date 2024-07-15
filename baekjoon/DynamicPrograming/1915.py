from sys import stdin
input = stdin.readline

n ,m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))

answer = 0
dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = 0 if arr[i][j] == '0' else 1
        elif arr[i][j] == '1' and dp[i - 1][j - 1] >= 1 and 1 <= dp[i - 1][j] and 1 <= dp[i][j - 1]:
            dp[i][j] = min([dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]]) + 1
        elif arr[i][j] == '1':
            dp[i][j] = 1
        answer = max(answer, dp[i][j])

print(answer * answer)