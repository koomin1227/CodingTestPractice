# https://www.acmicpc.net/problem/11779
from sys import stdin
import heapq
input = stdin.readline
INF=int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    s,e,c = map(int,input().split())
    graph[s].append([e,c])
start_city,end_city = map(int,input().split())

distance = [INF] * (n + 1)
prev_node = [0] * (n + 1)
course = []

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

dijkstra(start_city)
end = end_city
while True:
    if end == 0:
        break
    course.append(end)
    end = prev_node[end]
course.reverse()
print(distance[end_city])
print(len(course))
for i in course:
    print(i,end=' ')
