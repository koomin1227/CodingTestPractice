import heapq
INF = 100000
n,m = map(int, input().split())

graph = [[] for _ in range(n)]
dist = [INF] * n 
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append((b - 1, 1))
    graph[b - 1].append((a - 1, 1))

q = []
heapq.heappush(q, (0, 0))
dist[0] = 0

while q:
    cost, cur = heapq.heappop(q)
    if dist[cur] < cost:
        continue
    for nxt_node, nxt_cost in graph[cur]:
        res_cost = nxt_cost + cost
        if dist[nxt_node] > res_cost:
            dist[nxt_node] = res_cost
            heapq.heappush(q, (res_cost, nxt_node))

shed_dist = max(dist)
tmp = []
for i in range(len(dist)):
    if shed_dist == dist[i]:
        tmp.append(i)

shed_num = min(tmp) + 1
shed_cnt = len(tmp)

print(shed_num, shed_dist, shed_cnt)


