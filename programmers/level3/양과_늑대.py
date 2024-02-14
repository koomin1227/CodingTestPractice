def solution(info, edges):
    global answer
    answer = 1
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        a, b = edge
        graph[a].append(b)
    
    def dfs(now, sheep, wolf, movable):
        global answer
        if sheep == wolf:
            answer = max(sheep, answer)
            return
        for i in graph[now]:
            movable.append(i)
        if len(movable) == 0:
            answer = max(sheep, answer)
            return
        for i in movable:
            new_m = movable[:]
            new_m.remove(i)
            if info[i] == 0:
                dfs(i, sheep + 1, wolf, new_m)
            else:
                dfs(i, sheep, wolf + 1, new_m)
    dfs(0, 1, 0, [])
    return answer