#https://www.acmicpc.net/problem/1865
from sys import stdin
input=stdin.readline
INF=int(1e9)

T=int(input())
for t in range(T):
    n,m,w=map(int,input().split())
    cycle=[0]*(n+1)
    edges=[]
    negative_circle=0
    for i in range(m):
        a,b,c=map(int,input().split())
        edges.append([a,b,c])
        cycle[b]+=1
        edges.append([b,a,c])
        cycle[a]+=1
    for i in range(w):
        a,b,c=map(int,input().split())
        edges.append([a,b,c*(-1)])
        cycle[a]+=1
    # for k in range(1,n+1):
    #     if negative_circle==1:
    #         break
    #     if cycle[k]!=0:
    for i in range(1,n+1):
        if cycle[i]!=0:
            break
    dist=[INF]*(n+1)
    dist[i]=0
    for i in range(n):
        for j in range((2*m)+w):
            cur,next,cost=edges[j][0],edges[j][1],edges[j][2]
            if dist[cur]!=INF and dist[next]>dist[cur]+cost:
                dist[next]=dist[cur]+cost
                if i==n-1:
                    negative_circle=1
    if negative_circle==1:
        print('YES')
    else:
        print('NO')    
    

