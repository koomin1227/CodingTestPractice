def solution(edges):
    answer = [0,0,0,0]
    graph = {}
    for a,b in edges:
        if a not in graph:
            graph[a] = [0]
        if b not in graph:
            graph[b] = [0]
    for edge in edges:
        a,b = edge
        graph[a].append(b)
        graph[b][0] += 1
    for vertex in graph.keys():
        if graph[vertex][0] == 0 and len(graph[vertex]) >= 3:
            answer[0] = vertex
            break
    for start in graph[answer[0]][1:]:
        graph[start][0] -= 1
        d = start
        while True:
            if len(graph[d]) == 1:
                answer[2] += 1
                break
            if graph[d][0] == 2:
                answer[3] += 1
                break
            if graph[d][1] == start:
                answer[1] += 1
                break
            d = graph[d][1]
    return answer

# 생성한 정점 : 정점으로 향하는 간선이 없는 정점
# 막대 그래프 : 순회 하다가 더이상 이동할 정점이 없는 그래프
# 8자 그래프 : 순회 하다가 특정 정점으로 들어오는 간선이 2개인 그래프
# 도넛 그래프 : 순회 했을때 같은 정점으로 돌아오는 그래프