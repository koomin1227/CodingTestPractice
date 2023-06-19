import heapq
def solution(n, edge):
    answer = 0
    INF = 999999999
    graph = [[] for _ in range(n+1)]
    visited=[False]*(n+1)
    distance=[INF]*(n+1)
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    q=[]
    heapq.heappush(q,(0,1))
    distance[1]=0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist,now=heapq.heappop(q)
        #현재노드가 이미 처리 된적이 있다면 무시
        if distance[now]<dist:
            continue
        
        for i in graph[now]:
            cost=dist+1
            if cost<distance[i]:
                distance[i]=cost
                heapq.heappush(q,(cost,i))
    
    max_len = max(distance[2:])
    for i in distance[2:]:
        if i == max_len:
            answer +=1
    print(distance)
    return answer