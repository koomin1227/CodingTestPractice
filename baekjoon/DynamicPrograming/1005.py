#https://www.acmicpc.net/problem/1005
# 위상정렬 하여 위상순서를 구하고 다이나믹 으로 앞에서부터 최소찾기
from collections import deque
from sys import stdin
input=stdin.readline

t=int(input())
for i in range(0,t):
    #입력
    n,k=map(int,input().split())
    D=list(map(int,input().split()))#건설 속도
    graph=[[] for _ in range(n+1)]#그래프
    pregraph=[[] for _ in range(n+1)]#그래프
    indegree=[0 for _ in range(n+1)]#집입차수
    for j in range(0,k):
        a,b=map(int,input().split())
        graph[a].append(b)
        indegree[b]+=1

    w=int(input())
    dp=[0 for _ in range(n+1)]#다이나믹
    que=deque([])
    for i in range(1,len(indegree)):
        if indegree[i]==0:
            dp[i]=D[i-1]
            que.append(i)
    while(que):
        v=que.popleft()
        for j in graph[v]:
            indegree[j]-=1
            dp[j]=max(dp[j],dp[v]+D[j-1])
            if indegree[j]==0:
                que.append(j)
    print(dp[w])




        

    
