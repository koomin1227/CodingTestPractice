def solution(maze):
    global answer
    INF = 99999999999
    answer = INF
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    is_r_visit = [[0] * len(maze[0]) for _ in range(len(maze))]
    is_b_visit = [[0] * len(maze[0]) for _ in range(len(maze))]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                rp = [i,j]
            elif maze[i][j] == 2:
                bp = [i,j]
    
    def dfs(rp,bp, cnt):
        global answer
        # 최솟값보다 탐색한 방법이 더 많으면 탐색 중지
        if cnt > answer:
            return
        # 둘다 도착했으면 최솟값 업데이트
        if maze[rp[0]][rp[1]] == 3 and maze[bp[0]][bp[1]] == 4:
            answer = min(answer, cnt)
            return
        
        ry,rx = rp
        by,bx = bp
        for i in range(4):
            for j in range(4):
                r_move, b_move = True, True
                # 도착칸에 도착한 수레는 움직이지 않음
                nry, nrx = ry + dy[i], rx + dx[i]
                if maze[rp[0]][rp[1]] == 3:
                    nry, nrx, r_move = ry,rx,False
                nby, nbx = by + dy[j], bx + dx[j]
                if maze[bp[0]][bp[1]] == 4:
                    nby, nbx, b_move = by,bx,False
                
                # 판 넘어서 못지나감
                if nry < 0 or nry >= len(maze) or nrx < 0 or nrx >= len(maze[0]) or nby < 0 or nby >= len(maze) or nbx < 0 or nbx >= len(maze[0]):
                    continue
                # 벽으로 못 움직임
                if maze[nry][nrx] == 5 or maze[nby][nbx] == 5:
                    continue
                # 동시에 같은 칸으로는 못 움직임
                if nry == nby and nrx == nbx:
                    continue
                # 수레끼리 자리를 바꾸어 움직일 수 없음
                if nry == by and nrx == bx and nby == ry and nbx == rx:
                    continue
                # 지나온 자리로 움직일 수 없음
                if (is_r_visit[nry][nrx] == 'r' and r_move) or (is_b_visit[nby][nbx] == 'b' and b_move):
                    continue
                
                is_r_visit[nry][nrx], is_b_visit[nby][nbx] = 'r', 'b'
                dfs([nry,nrx], [nby, nbx], cnt + 1)
                is_r_visit[nry][nrx], is_b_visit[nby][nbx] = 0, 0
                
                
    is_r_visit[rp[0]][rp[1]], is_b_visit[bp[0]][bp[1]] = 'r', 'b'
    dfs(rp, bp, 0)
    if INF == answer:
        answer = 0
    return answer