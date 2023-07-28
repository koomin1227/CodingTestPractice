from sys import stdin
input=stdin.readline

n = int(input())
m =  int(input())
graph = [[] for _ in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])








