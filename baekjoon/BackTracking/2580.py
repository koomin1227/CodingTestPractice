#https://www.acmicpc.net/problem/2580
from sys import stdin
input = stdin.readline

sudoku = []
blank = []
for i in range(9):
    tmp = list(map(int,input().split()))
    for j in range(9):
        if tmp[j] == 0:
            blank.append([i,j])     
    sudoku.append(tmp)
num = len(blank)

def check(y,x,t):
    check = True
    for i in range(9):
        if t == sudoku[i][x]:
            return False
    for i in range(9):
        if t == sudoku[y][i]:
            return False
    for i in range(3 * (y // 3), 3 * (y // 3) + 3):
        for j in range(3 * (x // 3), 3 * (x // 3) + 3):
            if t == sudoku[i][j]:
                return False
    return True
def print_sudoku():
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j],end=" ")
        print()
sol = False
def dfs(cur):
    if cur == num:
        global sol
        sol = True
        print_sudoku()
        return
    y,x = blank[cur]
    for i in range(1,10):
        if check(y,x,i):
            sudoku[y][x] = i
            dfs(cur+1)
            sudoku[y][x] = 0
        if sol == True:
            break
dfs(0)

