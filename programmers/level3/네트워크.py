def solution(n, computers):
    answer = 0
    visit = [0]*n
    def dfs(node):
        visit[node] = 1
        for i in range(n):
            if computers[node][i] == 1 and visit[i] == 0:
                dfs(i)
    for i in range(n):
        if visit[i] == 0:
            dfs(i)
            answer += 1

    return answer
