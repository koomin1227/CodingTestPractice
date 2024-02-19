from collections import deque
def solution(board):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    # 왼, 하, 오, 상
    n = len(board)
    
    is_visit = [[[-1,-1,-1,-1] for _ in range(n)] for _ in range(n)]
    
    que = deque()
    que.append([0,0,0])
    is_visit[0][0][0] = 0
    while que:
        y1, x1, d = que.popleft()
        y2, x2 = y1 + direction[d][0], x1 + direction[d][1]
        # 상하좌우 이동
        for i in range(4):
            ny, nx = y1 + dy[i], x1 + dx[i]
            ny2, nx2 = y2 + dy[i], x2 + dx[i]
            
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if ny2 < 0 or ny2 >= n or nx2 < 0 or nx2 >= n:
                continue
            if is_visit[ny][nx][d] > -1:
                continue
            if board[ny2][nx2] == 1 or board[ny][nx] == 1:
                continue
            is_visit[ny][nx][d] = is_visit[y1][x1][d] + 1
            que.append([ny, nx, d])
        # 회전 이동1
        nds = [(d + 1) % 4, (d + 3) % 4]
        for nd in nds:
            ny1, nx1 = y1 + direction[nd][0], x1 + direction[nd][1]
            ny2, nx2 = y2 + direction[nd][0], x2 + direction[nd][1]
            if ny1 < 0 or ny1 >= n or nx1 < 0 or nx1 >= n:
                continue
            if board[ny1][nx1] == 1 or board[ny2][nx2] == 1:
                continue
            if is_visit[y1][x1][nd] > -1:
                continue
            is_visit[y1][x1][nd] = is_visit[y1][x1][d] + 1
            que.append([y1,x1,nd])
            
        # 회전 이동2
        nds = [(d + 1) % 4, (d + 3) % 4]
        for nd in nds:
            ny1, nx1 = y1 + direction[nd][0], x1 + direction[nd][1]
            ny2, nx2 = y2 + direction[nd][0], x2 + direction[nd][1]
            if ny1 < 0 or ny1 >= n or nx1 < 0 or nx1 >= n:
                continue
            if board[ny1][nx1] == 1 or board[ny2][nx2] == 1:
                continue
            if is_visit[y2][x2][nd] > 0:
                continue
            is_visit[y2][x2][nd] = is_visit[y1][x1][d] + 1
            que.append([y2,x2,nd])

    ans_list = []
    if is_visit[n-1][n-2][2] > -1:
        ans_list.append(is_visit[n-1][n-2][2])
    if is_visit[n-2][n-1][1] > -1:
        ans_list.append(is_visit[n-2][n-1][1])
    if is_visit[n-1][n-1][3] > -1:
        ans_list.append(is_visit[n-1][n-1][3])
    if is_visit[n-1][n-1][0] > -1:
        ans_list.append(is_visit[n-1][n-1][0])

    answer = min(ans_list)
    return answer