from sys import stdin
import heapq
INF=int(1e9)

n, m = map(int,input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
p, q = map(int,input().split())
homes = list(map(int, input().split()))
stores = list(map(int, input().split()))
heap = []
distances = [INF] * (n + 1)
for store in stores:
    heapq.heappush(heap, (0, store))
    distances[store] = 0
while heap:
    dist, now = heapq.heappop(heap)
    if distances[now] < dist:
        continue
    for next_v, weight in graph[now]:
        cost = dist + weight
        if distances[next_v] > cost:
            distances[next_v] = cost
            heapq.heappush(heap, (cost, next_v))
min_dist = INF
answer = 0
homes.sort()
for home in homes:
    if min_dist > distances[home]:
        min_dist = distances[home]
        answer = home
print(answer)