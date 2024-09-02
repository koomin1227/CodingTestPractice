from sys import stdin
input = stdin.readline
dc = (0, 1, 0, -1)
dr = (-1, 0, 1, 0)

def is_all_clean(r, c):
    is_all_clean = True
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if room[nr][nc] == 0:
            is_all_clean = False
            break
    return is_all_clean

n, m = map(int, input().split())
r, c, d = map(int, input().split())

room = []
for i in range(n):
    room.append(list(map(int, input().split())))
clean_count = 0

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        clean_count += 1
    else:
        if is_all_clean(r, c):
            back_d = (d + 2) % 4
            nr, nc = r + dr[back_d], c + dc[back_d]
            if room[nr][nc] == 1:
                break
            else:
                r,c = nr, nc
        else:
            rotate_d = d - 1
            if rotate_d < 0:
                rotate_d = 3
            nr, nc = r + dr[rotate_d], c + dc[rotate_d]
            d = rotate_d
            if room[nr][nc] == 0:
                r,c = nr, nc
print(clean_count)