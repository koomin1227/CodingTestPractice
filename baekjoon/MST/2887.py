#https://www.acmicpc.net/problem/2887
from sys import stdin
from collections import deque
input=stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
v=int(input())
graph=[]
edges=[]
for i in range(v):
    x,y,z=map(int,input().split())
    graph.append([x,y,z,i])
for i in range(3):
    graph.sort(key=lambda x:x[i])
    before=graph[0][3]
    for j in range(1,v):
        cur=graph[j][3]
        edges.append([abs(graph[j][i]-graph[j-1][i]),before,cur])
        before=cur
# for i in range(v):
#     for j in range(v):
#         if i!=j:
#             cost=min(abs(graph[i][0]-graph[j][0]),abs(graph[i][1]-graph[j][1]),abs(graph[i][2]-graph[j][2]))
#             edges.append([cost,i,j])
graph=[]
edges.sort()
parent = [0] * (v + 1)
result=0
for i in range(1, v + 1):
    parent[i] = i
tot=[]
# 정렬된 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 두 노드의 루트 노드가 서로 다르다면 사이클이 발생하지 않은것이므로  
    if find_parent(parent, a) != find_parent(parent, b):
        # 신장 트리에 간선 추가
        union_parent(parent, a, b)
        result += cost
print(result)