from sys import stdin
import heapq
input=stdin.readline
INF=int(1e9)

n,m,x = map(int,input().split())
graph=[[]for _ in range(n+1)]
graph_re=[[]for _ in range(n+1)]


for i in range(m):
    a,b,t = map(int,input().split())
    graph[a].append([b,t])
    graph_re[b].append([a,t])

def dijkstra(start, graph):
    q=[]
    heapq.heappush(q,(0,start))
    dist = [INF] * (n+1)
    dist[start]=0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dis,now=heapq.heappop(q)
        #현재노드가 이미 처리 된적이 있다면 무시
        if dist[now]<dis:
            continue
        
        for i in graph[now]:
            cost=dis+i[1]
            if cost<dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return dist
dist_go = dijkstra(x,graph_re)
dist_come = dijkstra(x,graph)

answer = 0
for i in range(1,n+1):
    answer = max(answer,dist_go[i] + dist_come[i])
print(answer)
