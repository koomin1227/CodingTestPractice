#https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(100001)
input=sys.stdin.readline
def dfs(s):
    global tot,ans
    isVisit[s]=True
    cycle.append(s)
    now=graph[s]
    if isVisit[now]==True:
        if now in cycle:
            ans=ans+cycle[cycle.index(now):]
        return
    else:
        dfs(now)

    
T=int(input())
for t in range(T):
    ans=[]
    n=int(input())
    graph=[0]
    graph=graph+list(map(int,input().split()))
    isVisit=[False]*(n+1)
    for i in range(1,n+1):
        cycle=[]
        if isVisit[i]==False:
            dfs(i)
    print(n-len(ans))

    