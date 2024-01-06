from sys import stdin
input = stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(input())
forest = []
coordinate = []
dp = [[1] * (n) for _ in range(n)]
answer = 0
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        coordinate.append([tmp[j],i,j])
    forest.append(tmp)
coordinate.sort(reverse=True)

for bamboo_amount,x,y in coordinate:
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx < 0 or nx >= n or ny < 0 or ny >= n):
            continue
        if forest[nx][ny] <= bamboo_amount:
            continue
        dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
    answer = max(answer, dp[x][y])
print(answer)

# 칸의 좌표를 큰 순으로 정렬 : nlog(n)
# 큰 좌표부터 dfs를 통해 최대 값을 찾고 기록
# 이 때 찾을 때 이미 찾아둔 정보를 이용해서 찾는다.

# 칸의 개수 : 250000 