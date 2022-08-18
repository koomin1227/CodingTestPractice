#https://www.acmicpc.net/problem/1504
from sys import stdin
from collections import deque
from itertools import combinations
import copy
import heapq
input=stdin.readline
INF=int(1e9)
n,e=map(int,input().split())#정점,간선
graph=[[] for _ in range(n+1)]
for i in range(e):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
v1,v2=map(int,input().split())
distance1=[INF]*(n+1)
distancev1=[INF]*(n+1)
distancev2=[INF]*(n+1)
def dijkstra(start,distance):
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
    return distance
distance1=dijkstra(1,distance1)
distancev1=dijkstra(v1,distancev1)
distancev2=dijkstra(v2,distancev2)
v1v2=distance1[v1]+distancev1[v2]+distancev2[n]
v2v1=distance1[v2]+distancev2[v1]+distancev1[n]
if v2v1>=INF or v1v2>=INF:
    print(-1)
else:
    print(min(v2v1,v1v2))

