from collections import deque
def solution(land):
    dx = [-1, 0, 1, 0]
    dy = [ 0, 1, 0, -1]
    len_y = len(land)
    len_x = len(land[0])
    oil = [0] * (len_x)
    is_visit = [[0] * (len_x) for i in range(len_y)]
    
    for i in range(len_y):
        for j in range(len_x):
            if land[i][j] == 1 and is_visit[i][j] == 0:
                que = deque()
                que.append([i, j])
                is_visit[i][j] = 1
                width = set([j])
                size = 1
                while que:
                    y, x = que.popleft()
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if ny < 0 or ny >= len_y or nx < 0 or nx >= len_x:
                            continue
                        if land[ny][nx] == 0:
                            continue
                        if is_visit[ny][nx] == 1:
                            continue
                        que.append([ny,nx])
                        is_visit[ny][nx] = 1
                        width.add(nx)
                        size += 1
                for w in width:
                    oil[w] += size
                
    answer = max(oil)            
    return answer