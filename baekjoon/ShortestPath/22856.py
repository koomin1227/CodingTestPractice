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

n = int(input())
graph = [[] for _ in range(n + 1)]
friend_location = list(map(int, input().split()))
m = int(input())
for i in range(m):
    a,b,w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

friend_distances = []
max_distance_location = 1000000
max_distance = 0
for location in friend_location:
    friend_distances.append(dijkstra(location, graph))

for i in range(1, n + 1):
    if i in friend_location:
        continue
    distance_from_friend = INF

    for distance in friend_distances:
        distance_from_friend = min(distance_from_friend, distance[i])

    if max_distance < distance_from_friend:
        max_distance = distance_from_friend
        max_distance_location = i
    elif max_distance == distance_from_friend:
        max_distance_location = min(max_distance_location, i)

print(max_distance_location)
