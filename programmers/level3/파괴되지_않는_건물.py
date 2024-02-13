def solution(board, skill):
    answer = 0
    r = len(board)
    c = len(board[0])
    damages = [[0] * (c + 1) for _ in range(r + 1)]
    res = [[0] * (c) for _ in range(r)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            damage = degree * -1
        else:
            damage = degree
        damages[r1][c1] += damage
        damages[r1][c2 + 1] -= damage
        damages[r2 + 1][c1] -= damage
        damages[r2 + 1][c2 + 1] += damage

    for i in range(r):
        for j in range(c):
            res[i][j] = damages[i][j]
            if i != 0:
                res[i][j] += res[i - 1][j]
            if j != 0:
                res[i][j] += res[i][j - 1]
            if i >= 1 and j >= 1:
                res[i][j] -= res[i - 1][j - 1]
            board[i][j] += res[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer