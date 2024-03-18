from sys import stdin
input = stdin.readline
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n,m,k = map(int, input().split())
land = [[[] for _ in range(n)] for _ in range(n)]
nourishment = []
nourishment_status = [[5] * n for _ in range(n)]
for i in range(n):
    nourishment.append(list(map(int, input().split())))
trees = {}
tree_num = 0
for i in range(m):
    x,y,z = map(int, input().split())
    trees[tree_num] = [[x - 1,y - 1], z, True]
    land[x - 1][y - 1].append(tree_num)
    tree_num += 1

for _ in range(k):
    #봄
    for i in range(n):
        for j in range(n):
            if len(land[i][j]) == 0:
                continue
            land[i][j].sort()
            for tree in land[i][j]:
                if nourishment_status[i][j] < trees[tree][1]:
                    trees[tree][2] = False
                else:
                    nourishment_status[i][j] -= trees[tree][1]
                    trees[tree][1] += 1
    # 여름
    for tree in list(trees.keys()):
        if trees[tree][2]:
            continue
        tree_x, tree_y = trees[tree][0]
        nourishment_status[tree_x][tree_y] += trees[tree][1] // 2
        land[tree_x][tree_y].remove(tree)
        del trees[tree]

    # 가을
    for tree in list(trees.keys()):
        if trees[tree][1] % 5 != 0:
            continue
        tree_x, tree_y = trees[tree][0]
        for i in range(8):
            nx, ny = tree_x + dx[i], tree_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            trees[tree_num] = [[nx,ny], 1, True]
            land[nx][ny].append(tree_num)
            tree_num += 1


    # 겨울
    for i in range(n):
        for j in range(n):
            nourishment_status[i][j] += nourishment[i][j]

print(len(trees))


