from sys import stdin
from itertools import combinations
from collections import deque
input = stdin.readline
dr = [0,-1,0]
dc = [-1,0,1]

n,m,d = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def find_nearest_enemy(board, cur_r, archer_position):
    que = deque()
    que.append((cur_r, archer_position[1], 1))

    while que:
        r,c,cur_d = que.popleft()
        if board[r][c] == 1:
            return (r,c)
        if cur_d < d:
            for i in range(3):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<n and 0<=nc<m:
                    que.append((nr, nc, cur_d + 1))

def simulate(archer_location):
    s_board = [row[:] for row in board]
    enemy_count = 0
    
    for r in range(n - 1, -1, -1):
        enemies = set()
        archer_r = r + 1

        for archer_c in archer_location:
            nearest_enemy = find_nearest_enemy(s_board, r, (archer_r, archer_c))
            if nearest_enemy != None:
                enemies.add(nearest_enemy)

        enemy_count += len(enemies)
        for enemy in enemies:
            s_board[enemy[0]][enemy[1]] = 0
    
    return enemy_count



answer = 0
archer_locations = combinations(range(m), 3)

for location in archer_locations:
    count = simulate(location)
    answer = max(answer, count)
    
print(answer)