import heapq
def solution(n, paths, gates, summits):
    INF=int(1e9)
    graph = [[] for _ in range(n)]
    intensity = [INF] * n
    node = [0] * n
    for i in summits:
        node[i - 1] = 2
    for a,b,c in paths:
        graph[a - 1].append([b - 1,c])
        graph[b - 1].append([a - 1,c])
    # 다익스트라
    heap = []
    for i in gates:
        heapq.heappush(heap, (0, i - 1))
        intensity[i - 1] = 0
    while heap:
        itst, now = heapq.heappop(heap)
        if intensity[now] < itst or node[now] == 2:
            continue
        for i in graph[now]:
            cost = max(itst, i[1])
            if cost < intensity[i[0]]:
                intensity[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
    # 최소 산봉우리
    answer = [0, INF]
    summits.sort()
    for i in summits:
        if answer[1] > intensity[i - 1]:
            answer[0] = i
            answer[1] = intensity[i - 1]
    return answer