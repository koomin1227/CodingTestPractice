from sys import stdin
import heapq

INF=int(1e9)
v, m = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

j, s = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (v + 1)
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
                heapq.heappush(q,(cost,i[0]))
    return distance

j_distance = dijkstra(j)
s_distance = dijkstra(s)

min_distance = INF

for i in range(1, v + 1):
    if i in [s,j]:
        continue
    min_distance = min(j_distance[i] + s_distance[i], min_distance)

appointment_place = -1
j_d = INF

for i in range(v, 0, -1):
    if i in [s,j]:
        continue
    if j_distance[i] + s_distance[i] == min_distance and j_distance[i] <= s_distance[i]:
        if j_d >= j_distance[i]:
            j_d = j_distance[i]
            appointment_place = i

print(appointment_place)
    