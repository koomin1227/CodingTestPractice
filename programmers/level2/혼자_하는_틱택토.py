def solution(board):
    ways = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],
            [(0,0), (1,0), (2,0)],[(0,1), (1,1), (2,1)],[(0,2), (1,2), (2,2)],
            [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]
           ]
    answer = 1
    o_list = []
    x_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_list.append((i, j))
            elif board[i][j] == 'X':
                x_list.append((i, j))

    if len(x_list) > len(o_list):
        return 0
    if len(o_list) - len(x_list) > 1:
        return 0

    
    o_win = False
    x_win = False
    for way in ways:
        o_count = 0
        x_count = 0
        for i, j in way:
            if board[i][j] == 'O':
                o_count += 1
            if board[i][j] == 'X':
                x_count += 1
        if o_count == 3 :
            o_win = True
        if x_count == 3:
            x_win = True
            
    if o_win and x_win:
        return 0
    if o_win and len(o_list) == len(x_list):
        return 0
    if x_win and len(o_list) != len(x_list):
        return 0
    return answer