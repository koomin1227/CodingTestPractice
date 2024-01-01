from sys import stdin
input = stdin.readline

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
tot = 0
for c in range(2):
    if c==1:
        board = list(map(list, zip(*board)))
    slope = [[0] * (n) for _ in range(n)] 
    for i in range(n):
        is_pass = 1
        for j in range(n):
            if j > 0 and board[i][j - 1] - board[i][j] == 1:
                is_pass2 = 1
                for k in range(j,j + l):
                    if (k >= n) or (board[i][j] != board[i][k]) or (slope[i][k] == 1):
                        is_pass2 = 0
                        break
                if is_pass2 == 1:
                    for k in range(j,j + l):
                        slope[i][k] = 1
                else:
                    is_pass = 0
                    break
            if j < n - 1 and board[i][j + 1] - board[i][j] == 1:
                is_pass2 = 1
                for k in range(j,j - l, -1):
                    if (k < 0) or (board[i][j] != board[i][k]) or (slope[i][k] == 1):
                        is_pass2 = 0
                        break
                if is_pass2 == 1:
                    for k in range(j,j - l, -1):
                        slope[i][k] = 1
                else:
                    is_pass = 0
                    break
            if j > 0 and board[i][j - 1] - board[i][j] > 1:
                is_pass = 0
                break
            if j < n - 1 and board[i][j + 1] - board[i][j] > 1:
                is_pass = 0
                break
        if is_pass == 1:
            tot += 1              
print(tot)