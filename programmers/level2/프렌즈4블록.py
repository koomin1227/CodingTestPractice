def solution(m, n, board):
    answer = 0
    bo = []
    for b in board:
        bo.append(list(b))
    
    while True:
        delete_area = []
        is_delete = False
        # 지울것 찾기
        for i in range(m - 1):
            for j in range(n - 1):
                if bo[i][j] == 0:
                    continue
                if bo[i][j] == bo[i][j + 1] and bo[i][j] == bo[i + 1][j] and bo[i][j] == bo[i + 1][j + 1]:
                    delete_area.append([i,j])
                    is_delete = True
        if is_delete == False:
            break
            
        # 지우기
        for y,x in delete_area:
            bo[y][x] = 0
            bo[y + 1][x] = 0
            bo[y][x + 1] = 0
            bo[y + 1][x + 1] = 0

        # 내리기
        new_board = [[0] * n for _ in range(m)]
        for j in range(n):
            idx = m - 1
            for i in range(m-1, -1, -1):
                if bo[i][j] != 0:
                    new_board[idx][j] = bo[i][j]
                    idx -= 1
        bo = new_board
        
    # 지워진 부분 세기
    for i in range(m):
        for j in range(n):
            if bo[i][j] == 0:
                answer += 1
    return answer