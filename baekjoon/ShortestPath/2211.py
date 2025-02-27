from sys import stdin
import heapq
INF = int(1e9)
input = stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
prev_node = [0] * (n + 1)
distance = [INF] * (n + 1)
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                prev_node[i[0]] = now
                heapq.heappush(q,(cost,i[0]))

dijkstra(1)

print(n - 1)
for i in range(2, n + 1):
    print(str(i) + ' ' + str(prev_node[i]))