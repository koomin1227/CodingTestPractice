from sys import stdin
input = stdin.readline

n = int(input())

board = [[0] * 101 for _ in range(101)]
inputs = []
for i in range(n):
    tmp = list(map(int,input().split()))
    inputs.append(tmp)
dx = [1,0,-1,0]
dy = [0,-1,0,1]
    

for i in inputs:
    degrees = [i[2]]
    for j in range(1,i[3] + 1):
        degree_len = len(degrees)
        for k in range(degree_len - 1, -1, -1):
            degrees.append((degrees[k] + 1) % 4)
    nx = i[0]
    ny = i[1]
    for j in degrees:
        board[ny][nx] = 1
        nx += dx[j]
        ny += dy[j]
    board[ny][nx] = 1

# 사각형세는 로직
tot = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            tot += 1
print(tot)
