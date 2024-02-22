from collections import deque
import heapq
def solution(board):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    # 좌, 상, 우, 하
    answer = 0
    def bfs(start):
        n = len(board)
        is_visit = [[100000000000000000] * n for _ in range(n)]
        que = deque()
        que.append(start)

        is_visit[0][0] = 0
        while que:
            c,y,x,d = que.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if ny < 0 or ny >=n or nx < 0 or nx >= n or board[ny][nx] == 1:
                    continue
                cost = c + 1
                if d != i:
                    cost += 5
                if cost <= is_visit[ny][nx]:
                    is_visit[ny][nx] = cost
                    que.append([cost,ny, nx,i])

        answer = is_visit[n-1][n-1] * 100
        return answer
    res = min(bfs([0,0,0,2]), bfs([0,0,0,3]))
    return res