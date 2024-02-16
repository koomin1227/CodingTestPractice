import heapq
def solution(n, s, a, b, fares):
    INF=int(1e9)
    answer = INF
    graph = [[] for _ in range(n + 1)]
    
    for fare in fares:
        c,d,f = fare
        graph[c].append((d,f))
        graph[d].append((c,f))
    
    def dijkstra(start, n):
        distance = [INF] * (n + 1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distance
    s_dist = dijkstra(s, n)
    a_dist = dijkstra(a, n)
    b_dist = dijkstra(b, n)
    
    # 합승 안 하는 경우
    answer = s_dist[a] + s_dist[b]
    # 합승하는 경우
    for i in range(1, n+1):
        cost = s_dist[i] + a_dist[i] + b_dist[i]
        answer = min(cost, answer)
    return answer

