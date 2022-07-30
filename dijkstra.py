import heapq
import sys 
input=sys.stdin.readline
INF=int(1e9)
#노드의 개수, 간선의 개수
n,m=map(int,input().split())
#시작할 노드의 번호
start=int(input())
#각 노드에 연결되 있는 노드에 대한 정보를 담는 리스트
graph=[[]for i in range(n+1)]
#최단 거리 테이블을 모두 무한 으로 초기화
distance=[INF]*(n+1)

#모든 간선 정보 입력
for _ in range(m):
    a,b,c=map(int,input().split())
    #a노드에서 b노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))


def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist,now=heapq.heappop(q)
        #현재노드가 이미 처리 된적이 있다면 무시
        if distance[now]<dist:
            continue
        
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))


dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print('INFINITY')
    else:
        print(distance[i])

"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""