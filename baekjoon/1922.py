from sys import stdin
import heapq
input=stdin.readline
INF = 1000000000

n = int(input())
m =  int(input())
graph = [[] for _ in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a-1].append([c,b-1])
    graph[b-1].append([c,a-1])

total_weight = 0
isVisited = set()
heap = []
mst_weights = [ INF for _ in range(len(graph)) ]
heapq.heappush(heap, [0, 0])
while len(heap) > 0:
    cur_vertex = heapq.heappop(heap)
    isVisited.add(cur_vertex[1])
    total_weight += cur_vertex[0]
    for vertex in graph[cur_vertex[1]]:
        node = vertex[1]
        weight = vertex[0]
        if node not in isVisited and weight < mst_weights[node]:
            heapq.heappush(heap, vertex)
            mst_weights[node] = weight

print(sum(mst_weights[1:]))



