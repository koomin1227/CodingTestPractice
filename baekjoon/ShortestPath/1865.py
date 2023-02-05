#https://www.acmicpc.net/problem/1865
from sys import stdin
input=stdin.readline
INF=int(1e9)

T=int(input())
for t in range(T):
    n,m,w=map(int,input().split())
    edges=[]
    negative_circle=0
    for i in range(m):
        a,b,c=map(int,input().split())
        edges.append([a,b,c])
        edges.append([b,a,c])
    for i in range(w):
        a,b,c=map(int,input().split())
        edges.append([a,b,c*(-1)])

    dist=[INF]*(n+1)
    dist[i]=0
    for i in range(n):
        for j in range((2*m)+w):
            cur,next,cost=edges[j][0],edges[j][1],edges[j][2]
            if dist[next]>dist[cur]+cost:
                dist[next]=dist[cur]+cost
                if i==n-1:
                    negative_circle=1
    if negative_circle==1:
        print('YES')
    else:
        print('NO')    
    

