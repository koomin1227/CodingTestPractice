from collections import deque
INF = 999999999999
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solution(board):
    answer = INF
    bord = []
    for i in range(len(board)):
        temp = list(board[i])
        bord.append(temp)
        for j in range(len(temp)):
            if temp[j] == 'R':
                r = (i, j)
                
    visited = [[-1] * (len(bord[0])) for _ in range(len(bord))]
    que = deque()
    que.append([r, 0])
    visited[r[0]][r[1]] = 0
    
    while que:
        coord, count = que.popleft()
        if bord[coord[0]][coord[1]] == 'G':
            answer = min(answer, count)
        for i in range(4):
            ny, nx = coord
            while True:
                ny += dy[i]
                nx += dx[i]
                if ny < 0 or ny >= len(bord) or nx < 0 or nx >= len(bord[0]) or bord[ny][nx] == 'D':
                    ny -= dy[i]
                    nx -= dx[i]
                    break

            if (visited[ny][nx] == -1) or (visited[ny][nx] != -1 and visited[ny][nx] > count + 1):
                visited[ny][nx] = count + 1
                que.append([(ny, nx), count + 1])


    if answer == INF:
        answer = -1
    return answer