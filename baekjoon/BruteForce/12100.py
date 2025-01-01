from sys import stdin
input = stdin.readline

def rotate_board(board, n, times):
    for _ in range(times):
        board = [[board[n - 1 - j][i] for j in range(n)] for i in range(n)]
    return board

        
def move_board(board, direction, n):
    new_board = [[0] * n for _ in range(n)]
    
    for i in range(n):
        stack = []
        index = 0
        if direction in ('left', 'right'): 
            range_iter = range(n) if direction == 'left' else range(n-1, -1, -1)
            for j in range_iter:
                if board[i][j] == 0:
                    continue
                if not stack:
                    stack.append(board[i][j])
                else:
                    if stack[-1] == board[i][j]:
                        if direction == 'left':
                            new_board[i][index] = stack.pop() * 2
                        else:
                            new_board[i][n-1-index] = stack.pop() * 2
                        index += 1
                    else:
                        if direction == 'left':
                            new_board[i][index] = stack.pop()
                        else:
                            new_board[i][n-1-index] = stack.pop()
                        index += 1
                        stack.append(board[i][j])
            if stack:
                if direction == 'left':
                    new_board[i][index] = stack.pop()
                else:
                    new_board[i][n-1-index] = stack.pop()
        
        elif direction in ('up', 'down'):
            range_iter = range(n) if direction == 'up' else range(n-1, -1, -1)
            for j in range_iter:
                if board[j][i] == 0:
                    continue
                if not stack:
                    stack.append(board[j][i])
                else:
                    if stack[-1] == board[j][i]:
                        if direction == 'up':
                            new_board[index][i] = stack.pop() * 2
                        else:
                            new_board[n-1-index][i] = stack.pop() * 2
                        index += 1
                    else:
                        if direction == 'up':
                            new_board[index][i] = stack.pop()
                        else:
                            new_board[n-1-index][i] = stack.pop()                        
                        index += 1
                        stack.append(board[j][i])
            if stack:
                if direction == 'up':
                    new_board[index][i] = stack.pop()
                else:
                    new_board[n-1-index][i] = stack.pop()
    
    return new_board

def dfs(depth, board,n):
    directions = ['up','down','left','right']
    if depth == 5:
        max_num = 0
        for b in board:
            max_num = max(max(b), max_num)
        return max_num
    answer = 0
    for i in range(4):
        new_board = move_board(board, directions[i], n)
        answer =  max(dfs(depth + 1, new_board, n), answer)
    return answer
    

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
print(dfs(0, board, n))