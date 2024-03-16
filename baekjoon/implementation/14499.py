from sys import stdin
input = stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
n,m,x,y,k = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
orders = list(map(int, input().split()))
dice = [0,0,0,0,0,0]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for order in orders:
    nx, ny = x + dx[order - 1], y + dy[order - 1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    x,y = nx,ny
    turn(order)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
    print(dice[0])

