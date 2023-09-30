from sys import stdin
input = stdin.readline

n = int(input())

board = [[0] * 100 for _ in range(100)]
inputs = []
for i in range(n):
    tmp = list(map(int,input().split()))
    inputs.append(tmp)
dx = [1,0,-1,0]
dy = [0,-1,0,1]
def rotate(d, t):
    if t%2 == 0:
        nd = d + 1
        if nd > 3:
            nd = 0
        return nd
    else:
        nd = d - 1
        if nd < 0:
            nd = 3
        return nd
        
def draw_dragon(x,y,d,g,t):
    if g == 0:
        board[y][x] = 1
        nx = x + dx[d]
        ny = y + dy[d]
        board[ny][nx] = 1
        nd = rotate(d, t)
        return [nx, ny, nd]
    else:
        nx , ny, nd = draw_dragon(x,y,d,g - 1,t)
        tmp =  draw_dragon(nx,ny,nd,g - 1,t)
        tmp[2] += 1
        return tmp



for tmp in inputs:
    draw_dragon(tmp[0],tmp[1],tmp[2],tmp[3],0)
# print(board)
