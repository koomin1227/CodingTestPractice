#https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(100001)
input=sys.stdin.readline
def dfs(s,t):
    global tot
    now=graph[s]
    if isVisit[now]==False or now==t:
        isVisit[now]=True
        tot+=1
        if now==t:
            return True
        if dfs(now,t)==False:
            isVisit[now]=False 
            tot-=1
            return False
        else:
            return True
    return False
T=int(input())
for t in range(T):
    ans=0
    n=int(input())
    graph=[0]
    graph=graph+list(map(int,input().split()))
    isVisit=[False]*(n+1)
    tot=0
    for i in range(1,n+1):
        if isVisit[i]==False:
            isVisit[i]=True
            tot+=1
            if dfs(i,i)==False:
                isVisit[i]=False
            tot-=1
    # for i in range(1,n+1):
    #     if isVisit[i]==False:
    #         ans+=1
    print(n-tot)

    