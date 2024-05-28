#https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
def dfs(s):
    global ans
    isVisit[s]=True
    cycle.append(s)
    now=graph[s]
    if isVisit[now]==True:
        if now in cycle:
            ans-=len(cycle[cycle.index(now):])
        return
    else:
        dfs(now)

    
T=int(input())
for t in range(T):
    n=int(input())
    ans=n
    graph=[0]
    graph=graph+list(map(int,input().split()))
    isVisit=[False]*(n+1)
    for i in range(1,n+1):
        if isVisit[i]==False:
            cycle=[]
            dfs(i)
    print(ans)

    