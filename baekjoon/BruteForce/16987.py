N = int(input())
eggs = []
for _ in range(N):
    eggs.append(list(map(int, input().split())))
answer = 0
def dfs(position):
    global answer
    if position == N:
        count = 0
        for egg in eggs:
            if egg[0] <= 0:
                count += 1
        answer = max(answer, count)
        return 
    cur_egg = eggs[position]
    if cur_egg[0] <= 0:
        dfs(position + 1)
    else:
        for i in range(N):
            if i == position:
                continue
            if eggs[i][0] <= 0:
                dfs(position + 1)
            else:
                cur_egg[0] -= eggs[i][1]
                eggs[i][0] -= cur_egg[1]
                dfs(position + 1)
                cur_egg[0] += eggs[i][1]
                eggs[i][0] += cur_egg[1]
dfs(0)
print(answer)