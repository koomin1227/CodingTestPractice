from sys import stdin
from collections import deque

dr = [0, 1, 0, -1] # 오, 아, 왼, 위
dc = [1, 0, -1, 0]

# 초기화
n, m = map(int, input().split())
board = []
b_position = []
r_position = []
hole_position = []
for i in range(n):
    tmp = list(input())
    board.append(tmp)
    for j in range(m):
        if tmp[j] == 'B':
            b_position = [i, j]
        elif tmp[j] == 'R':
            r_position = [i, j]
        elif tmp[j] == 'O':
            hole_position = [i, j]

def get_move_sequence(ball_positions, direction):
    red = ball_positions[0]
    blue = ball_positions[1]
    if direction == 0:
        if red[1] > blue[1]:
            return 'r'
        else:
            return 'b'
    elif direction == 2:
        if red[1] > blue[1]:
            return 'b'
        else:
            return 'r'
    elif direction == 1:
        if red[0] > blue[0]:
            return 'r'
        else:
            return 'b'
    elif direction == 3:
        if red[0] > blue[0]:
            return 'b'
        else:
            return 'r'
            

def move(ball_positions, direction):
    first_move = get_move_sequence([ball_positions['r'], ball_positions['b']], direction)
    if first_move == 'r':
        second_move = 'b'
    else:
        second_move = 'r'
    n_position = [ball_positions[first_move][0], ball_positions[first_move][1]]
    for i in range(10):
        n_position[0] += dr[direction]
        n_position[1] += dc[direction]
        if board[n_position[0]][n_position[1]] == '#':
            n_position[0] -= dr[direction]
            n_position[1] -= dc[direction]
            break
        elif board[n_position[0]][n_position[1]] == 'O':
            break
    ball_positions[first_move][0] = n_position[0]
    ball_positions[first_move][1] = n_position[1]

    n_position = [ball_positions[second_move][0], ball_positions[second_move][1]]
    for i in range(10):
        n_position[0] += dr[direction]
        n_position[1] += dc[direction]
        if board[n_position[0]][n_position[1]] == '#':
            n_position[0] -= dr[direction]
            n_position[1] -= dc[direction]
            break
        elif board[n_position[0]][n_position[1]] == 'O':
            break
        elif n_position[0] == ball_positions[first_move][0] and n_position[1] == ball_positions[first_move][1]:
            n_position[0] -= dr[direction]
            n_position[1] -= dc[direction]
            break
    ball_positions[second_move][0] = n_position[0]
    ball_positions[second_move][1] = n_position[1]

    return ball_positions    

que = deque()
que.append((tuple(r_position),tuple(b_position), 0))
is_visited = set()
is_visited.add((tuple(r_position),tuple(b_position)))
answer = 100000000000
while que:
    red, blue, cnt = que.popleft()
    if cnt > 10:
        continue

    if red[0] == hole_position[0] and red[1] == hole_position[1]:
        answer = min(answer, cnt)
        print(answer)
        break
    
    for d in range(4):
        ball_positions = move({'r': list(red), 'b': list(blue)}, d)
        n_red = ball_positions['r']
        n_blue = ball_positions['b']
        tuple_position = (tuple(n_red),tuple(n_blue))
        if tuple_position in is_visited:
            continue
        else:
            if n_red[0] == hole_position[0] and n_red[1] == hole_position[1] and n_blue[0] == hole_position[0] and n_blue[1] == hole_position[1]:
                continue
            elif n_blue[0] == hole_position[0] and n_blue[1] == hole_position[1]:
                continue
            is_visited.add((tuple(n_red), tuple(n_blue)))
            que.append((tuple(n_red), tuple(n_blue), cnt + 1))

if answer == 100000000000:
    print(-1)
