from collections import deque
def solution(board):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    # 왼, 위, 오, 아
    # 좌, 상, 우, 하
    answer = 0
    n = len(board)
    is_visit = [[-1] * n for _ in range(n)]
    que = deque()
    que.append([0,0,2])
    que.append([0,0,3])
    is_visit[0][0] = 0
    while que:
        y,x,d = que.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >=n or nx < 0 or nx >= n:
                continue
            if board[ny][nx] == 1:
                continue
            # if is_visit[ny][nx] > -1:
            #     continue
            cost = is_visit[y][x] + 1
            if d != i:
                cost += 5
            if is_visit[ny][nx] == -1 or cost < is_visit[ny][nx]:
                is_visit[ny][nx] = cost
                que.append([ny, nx,i])
    for i in is_visit:
        print(i)
    return answer

board = [[0,0,0],[0,0,0],[0,0,0]]

solution(board)