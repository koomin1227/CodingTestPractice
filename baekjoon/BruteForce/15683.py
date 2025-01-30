dx = [0,1,0,-1]
dy = [1,0,-1,0]
ds = [
    [[0],[1],[2],[3]],
    [[0,2], [1,3]],
    [[0,1], [1,2], [2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]

n ,m = map(int, input().split())
office = []
cctvs = []



for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] in [1,2,3,4,5]:
            cctvs.append([tmp[j], i, j, 0])
    office.append(tmp)

answer = n*m
masking = -1

def dfs(depth):
    global masking
    global answer
    if depth == len(cctvs):
        dead_zone_cnt = check_office(cctvs, masking)
        masking -= 1
        answer = min(answer, dead_zone_cnt)
        return
    if cctvs[depth][0] in [1,3,4]:
        for i in range(4):
            cctvs[depth][3] = i
            dfs(depth + 1)
    elif cctvs[depth][0] == 2:
        for i in range(2):
            cctvs[depth][3] = i
            dfs(depth + 1)
    else:
        dfs(depth + 1)

def check_office(cctvs, masking):
    dead_zone_cnt = 0
    for cctv_num, y, x, d in cctvs:
        directions = ds[cctv_num - 1][d]
        for direction in directions:
            ny = y
            nx = x
            while True:
                ny = ny + dy[direction]
                nx = nx + dx[direction]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    break
                elif office[ny][nx] == 6:
                    break
                elif office[ny][nx] in [1,2,3,4,5]:
                    continue
                office[ny][nx] = masking
    for i in office:
        for j in i:
            if j != masking and j not in [1,2,3,4,5,6]:
                dead_zone_cnt += 1
    return dead_zone_cnt

dfs(0)
print(answer)
