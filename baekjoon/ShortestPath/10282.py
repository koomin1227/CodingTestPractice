from sys import stdin
import heapq
INF = 10000000000000000

input = stdin.readline
def dijkstra(start, graph):
    q=[]
    heapq.heappush(q,(0,start))
    dist = [INF] * (n+1)
    dist[start]=0
    while q:
        dis,now=heapq.heappop(q)
        if dist[now]<dis:
            continue
        
        for i in graph[now]:
            cost=dis+i[1]
            if cost<dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return dist

t = int(input())
answer = []
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a,s))
    dist = dijkstra(c, graph)
    infected_count = 0
    last_infected_time = 0
    for i in range(1, n + 1):
        if dist[i] < INF:
            infected_count += 1
            last_infected_time = max(last_infected_time, dist[i])
    answer.append([infected_count, last_infected_time])

for ans in answer:
    print(ans[0], ans[1])

# 2
# 3 2 2
# 2 1 5
# 3 2 5
# 3 3 1
# 2 1 2
# 3 1 8
# 3 2 4