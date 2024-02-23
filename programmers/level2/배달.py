import heapq
INF = 100000000000
def solution(N, road, K):
    answer = 0

    graph = [[] for _ in range(N + 1)]
    for r in road:
        a,b,c = r
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    distance = [INF] * (N + 1)
    que = []
    heapq.heappush(que, (0, 1))
    distance[1] = 0
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for b, c in graph[now]:
            cost = dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(que, (cost, b))
    for d in distance:
        if d <= K:
            answer += 1

    return answer

